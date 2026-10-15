
# RFI Triage Agent - GC Team 7

import json
import os
import time
from google import genai
from google.genai import types, errors


client = genai.Client()


def convert_priority(priority):
    priority_map = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    if isinstance(priority, str):
        priority = priority_map.get(priority.lower(), priority)

    if priority in (1, 2, 3):
        return priority

    return None


def triage_rfi(rfi):
    prompt = f"""
You are an RFI triage assistant for a construction project.

Analyze the RFI below and classify it based on
the information provided. Do not make up facts.

RFI ID: {rfi['rfi_id']}
Question: {rfi['question']}

Return a JSON object with these fields:
- rfi_id
- needs_response (true or false)
- root_cause
- responder
- due
- contractual_risk (low, medium, or high)
- risk_reason
- priority (integer: 1 = high, 2 = medium, 3 = low)
- duplicate_of (null if unknown)

Use only these root_cause categories:
- doc_conflict: conflicting information in documents
- missing_info: missing details or requirements
- scope_split: unclear responsibility or scope
- duplicate: question already raised in another RFI
- ambiguity: unclear wording or specifications
- third_party: issue involving an outside organization

For responder, use one of:
- architect
- contracting_officer
- civil
- electrical
- fire_protection
- multiple

For due, use one of:
- before_proposal_due
- next_amendment

Priority must be an integer:
1 = high priority
2 = medium priority
3 = low priority

Consider project cost, schedule, safety, and
contractual impact when assigning priority.

If the available information is insufficient,
use null rather than guessing.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            result = json.loads(response.text)
            result["priority"] = convert_priority(
                result.get("priority")
            )

            return result

        except errors.ServerError as e:
            if e.code != 503 or attempt == 2:
                raise

            print("Gemini is busy. Retrying...", flush=True)
            time.sleep(5 * (attempt + 1))


if __name__ == "__main__":
    with open("data/rfi_test_set.json", "r") as file:
        rfis = json.load(file)

    print(f"Loaded {len(rfis)} RFIs", flush=True)

    output_file = "data/agent_results.json"
    results = []

    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            results = json.load(file)

    for result in results:
        result["priority"] = convert_priority(
            result.get("priority")
        )

    with open(output_file, "w") as file:
        json.dump(results, file, indent=2)

    for rfi in rfis:
        if any(
            str(r["rfi_id"]) == str(rfi["rfi_id"])
            for r in results
        ):
            print(
                f"Skipping RFI #{rfi['rfi_id']} (already processed)",
                flush=True
            )
            continue

        print(f"Analyzing RFI #{rfi['rfi_id']}...", flush=True)

        try:
            result = triage_rfi(rfi)
            results.append(result)
            print(json.dumps(result, indent=2), flush=True)

        except Exception as e:
            print(
                f"RFI #{rfi['rfi_id']} failed: {e}",
                flush=True
            )

        with open(output_file, "w") as file:
            json.dump(results, file, indent=2)

    print(
        f"Finished! {len(results)}/{len(rfis)} RFIs completed.",
        flush=True
    )
