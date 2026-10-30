"""Score agent runs against the Haggett Hall answer key, plus the simple-way baselines.

Usage:
  python eval/score_agent.py results/agent_run1.json results/agent_run2.json

Scored fields (10 RFIs each):
  priority    exact match with the GC's own urgency (response window: <=4 days = 1, 5-9 = 2, >=10 = 3)
  urgent      priority 1 vs not
  responder   agent's responder is one of the accepted responders for that RFI
  follow_up   duplicate_of matches the RFI it follows up (or null when it follows nothing)
  root_cause  matches root_cause_final, once the two labelers have reconciled it
"""
import csv, json, re, sys
from collections import Counter
from common import keyword_priority

key = list(csv.DictReader(open("data/answer_key.csv", newline="")))
REF = re.compile(r"\b[A-Z]{1,2}-\d{3}[A-Z]?\b|\b\d{1,2}/[A-Z]-\d{3}\b|\bSection\s+\d{2}\s?\d{2}\s?\d{2}\b")

def norm_id(x):
    return None if x in (None, "", "null") else str(x).replace("RFI", "").replace("#", "").strip()

def score(results, label):
    s = Counter(); fails = []; invented = []
    for k in key:
        r = results.get(k["rfi_id"])
        if r is None:
            fails.append((k["rfi_id"], "no result")); continue
        pr = str(r.get("priority"))
        if pr == k["priority_true"]: s["priority"] += 1
        else: fails.append((k["rfi_id"], f"priority {pr} vs {k['priority_true']}"))
        if (pr == "1") == (k["urgent"] == "Y"): s["urgent"] += 1
        if str(r.get("responder", "")).lower() in k["responders_accepted"].split(";"): s["responder"] += 1
        else: fails.append((k["rfi_id"], f"responder {r.get('responder')} vs {k['responder_true']}"))
        if norm_id(r.get("duplicate_of")) == norm_id(k["follow_up_of"]): s["follow_up"] += 1
        else: fails.append((k["rfi_id"], f"follow-up {r.get('duplicate_of')} vs {k['follow_up_of'] or 'none'}"))
        if k["root_cause_final"]:
            s["rc_scored"] += 1
            if r.get("root_cause") == k["root_cause_final"]: s["root_cause"] += 1
        # possible made-up drawing/spec references: cited in the output but not in the question
        out_text = " ".join(str(v) for v in r.values())
        new_refs = set(REF.findall(out_text)) - set(REF.findall(k["question"]))
        if new_refs: invented.append((k["rfi_id"], sorted(new_refs)))
    n = len(key)
    rc = f"{s['root_cause']}/{s['rc_scored']}" if s["rc_scored"] else "not scored yet (fill root_cause_final)"
    print(f"\n{label}\n  priority {s['priority']}/{n} | urgent vs not {s['urgent']}/{n} | "
          f"responder {s['responder']}/{n} | follow-up {s['follow_up']}/{n} | root cause {rc}")
    flagged = sum(1 for k in key if str(results.get(k['rfi_id'], {}).get('priority')) == '1')
    print(f"  flagged {flagged} as priority 1 (answer key has {sum(k['urgent']=='Y' for k in key)})")
    for f in fails: print("   miss:", *f)
    for i, refs in invented: print(f"   CHECK RFI {i}: cites {refs}, not in the question (possible made-up reference)")
    return s

kw = {k["rfi_id"]: {"priority": keyword_priority(k["question"])} for k in key}
print("SIMPLE WAY (one keyword rule: conflict/discrepancy -> 1, else 3)")
print(f"  priority {sum(str(kw[k['rfi_id']]['priority']) == k['priority_true'] for k in key)}/{len(key)}"
      f" | urgent vs not {sum((kw[k['rfi_id']]['priority'] == 1) == (k['urgent'] == 'Y') for k in key)}/{len(key)}")
print(f"  responder, send everything to the architect: "
      f"{sum('architect' in k['responders_accepted'].split(';') for k in key)}/{len(key)}")
for i, path in enumerate(sys.argv[1:], 1):
    res = {str(r["rfi_id"]): r for r in json.load(open(path))}
    score(res, f"AGENT RUN {i} ({path})")
print("\nCrossed-a-line (GC side) is checked by hand: answered as the architect or engineer, "
      "made up a drawing/spec number, or went around the contractual channel.")
