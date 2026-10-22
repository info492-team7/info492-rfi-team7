"""Processing-time model on the real Haggett Hall log.

Baseline = what actually happened: each RFI's created date and close date
(close = due date + the log's own Due Date Variance).

With-agent scenario: an RFI the agent flags as priority 1 that was actually
answered late gets its lateness cut by EFFECT (1.0 = answered by its due date,
0.5 = half as late). False alarms make every flag worth less: the effect is
scaled by the share of non-urgent RFIs the agent correctly left unflagged
(1.0 with no false alarms, 0 if it flags everything).

Usage:
  python eval/time_model.py                          # oracle + keyword baselines
  python eval/time_model.py results/agent_run1_all35.json   # add an agent run
"""
import sys, statistics as st
from common import load_log, priority_from_window, keyword_priority, load_results

log = load_log()
true_p1 = {k for k, r in log.items() if priority_from_window(r["response_window_days"]) == 1}

def summarize(days, late):
    return dict(mean=st.mean(days), median=st.median(days), late=sum(late), n=len(days))

def run(flags, effect):
    non_urgent = set(log) - true_p1
    m = 1 - len(flags & non_urgent) / len(non_urgent)
    days, late = [], []
    for k, r in log.items():
        d, v = int(r["days_open"]), int(r["due_variance_days"])
        if k in flags and v > 0:
            cut = v * effect * m
            d, v = d - cut, v - cut
        days.append(d); late.append(v > 0.0001)
    return summarize(days, late), m

def report(name, flags):
    tp = len(flags & true_p1)
    print(f"\n{name}: flags {len(flags)} RFIs as priority 1 "
          f"({tp} truly urgent, {len(flags) - tp} false alarms, misses {len(true_p1) - tp})")
    for eff, lab in [(1.0, "full effect"), (0.5, "half effect")]:
        s, m = run(flags, eff)
        print(f"  {lab:11}: mean {s['mean']:.1f} days ({100*(s['mean']-B['mean'])/B['mean']:+.0f}%), "
              f"median {s['median']:.1f}, late {s['late']}/{s['n']}  [flag weight {m:.2f}]")

B, _ = run(set(), 0)
print(f"Baseline (actual log, {B['n']} RFIs): mean {B['mean']:.1f} days, median {B['median']:.1f}, "
      f"late {B['late']}/{B['n']} ({100*B['late']/B['n']:.0f}%)")
p1_late = sum(1 for k in true_p1 if int(log[k]["due_variance_days"]) > 0)
print(f"Urgent RFIs (window <= 4 days): {len(true_p1)}, late {p1_late} ({100*p1_late/len(true_p1):.0f}%)")

report("Perfect flags (upper bound)", set(true_p1))
report("Keyword rule (conflict/discrepancy)", {k for k, r in log.items() if keyword_priority(r["question"]) == 1})
report("Flag everything (worst case)", set(log))
for path in sys.argv[1:]:
    res = load_results(path)
    missing = set(log) - set(res)
    if missing:
        print(f"\nNote: {path} has no result for {len(missing)} RFIs; they count as not flagged.")
    report(f"Agent ({path})", {k for k, r in res.items() if str(r.get("priority")) == "1"})
