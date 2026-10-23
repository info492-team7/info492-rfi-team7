
# RFI Triage Agent - GC Team 7
# Demo 2 - Haggett Hall

import json
import os
import sys
import time
from google import genai
from google.genai import types, errors


client = genai.Client()


def convert_priority(priority):
    priority_map = {
        "high": 1,
        "medium": 2,
        "low": 3,
        "1": 1,
        "2": 2,
        "3": 3
    }

    if isinstance(priority, str):
        priority = priority_map.get(priority.lower().strip())

    if priority in (1, 2, 3):
        return priority

    return None


def get_earlier_rfis(rfi, all_rfis):
    earlier = []
    current_id = str(rfi["rfi_id"])

    for item in all_rfis:
        if str(item["rfi_id"]) == current_id:
            break

        # Same-day RFIs follow the order in the log.
        # Do not include records from later dates.
        if item["created"] <= rfi["created"]:
            earlier.append({
                "rfi_id": item["rfi_id"],
                "question": item["question"]
            })

    return earlier


def triage_rfi(rfi, earlier_rfis):
    history = json.dumps(earlier_rfis, ensure_ascii=False)

    prompt = f"""
You are an RFI triage assistant for the Haggett Hall
construction project.

These RFIs are construction-phase questions from the
general contractor to the design team.

Read the full RFI question and classify it based only
on the information provided. Do not make up facts.

RFI ID: {rfi['rfi_id']}
Question: {rfi['question']}

Earlier RFIs:
{history}

Return a JSON object with these fields:
- rfi_id
- needs_response (true or false)
- root_cause
- responder
- due
- contractual_risk (low, medium, or high)
- risk_reason
- priority (integer: 1, 2, or 3)
- duplicate_of (earlier RFI number or null)

Use only these root_cause categories:

- field_condition:
  Unexpected site conditions that drawings did not anticipate,
  such as existing utilities, soil, or footings.

- design_conflict:
  Two drawings, disciplines, or building elements conflict.

- missing_info:
  Drawings or specifications are missing necessary dimensions,
  elevations, locations, or other information.

- contractor_proposal:
  The GC or subcontractor proposes a change or substitution
  and asks the design team for approval.

Choose the one root cause that best explains the question.

For responder, use only:
- architect
- structural
- civil
- geotechnical
- mechanical_electrical
- landscape
- multiple

Assign priority based on urgency:

1 = Field work is waiting for an answer.
    Response needed within about 3 days.

2 = A response is needed soon, within about 7 days.

3 = The issue can wait about 14 days.

Do not classify an RFI as priority 1 just because
it mentions cost, risk, or a design conflict.

Only assign priority 1 when the question suggests
that field work is waiting or needs an immediate answer.

Use the question text to estimate urgency.
Do not use actual response dates to decide priority.

For due, return the number of days:
- Priority 1: 3
- Priority 2: 7
- Priority 3: 14

For contractual_risk, choose low, medium, or high.
Explain the reason briefly in risk_reason.

For duplicate_of, compare the current question with
the earlier RFIs provided above.

If the question is a follow-up or continuation of an
earlier RFI, return that earlier RFI number as a string.

If there is no clear relationship, return null.

Only use RFI numbers from the earlier RFI list.
Do not invent an RFI number.

Keep the original RFI ID in the output.
Do not paraphrase the question when analyzing it.

Return only the JSON object.
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

            result["rfi_id"] = str(rfi["rfi_id"])

            result["priority"] = convert_priority(
                result.get("priority")
            )

            if result["priority"] is None:
                raise ValueError("Invalid priority returned")

            result["due"] = {
                1: 3,
                2: 7,
                3: 14
            }[result["priority"]]

            # Check that the categories match the scoring rules.
            valid_causes = (
                "field_condition",
                "design_conflict",
                "missing_info",
                "contractor_proposal"
            )

            valid_responders = (
                "architect",
                "structural",
                "civil",
                "geotechnical",
                "mechanical_electrical",
                "landscape",
                "multiple"
            )

            if result.get("root_cause") not in valid_causes:
                raise ValueError("Invalid root cause returned")

            if result.get("responder") not in valid_responders:
                raise ValueError("Invalid responder returned")

            duplicate = result.get("duplicate_of")

            if duplicate is not None:
                duplicate = str(duplicate).replace(
                    "RFI", ""
                ).replace("#", "").strip()

                earlier_ids = {
                    str(item["rfi_id"]) for item in earlier_rfis
                }

                if duplicate not in earlier_ids:
                    duplicate = None

            result["duplicate_of"] = duplicate

            return result

        except errors.ServerError as e:
            if e.code != 503 or attempt == 2:
                raise

            print(
                "Gemini is busy. Retrying...",
                flush=True
            )
            time.sleep(5 * (attempt + 1))


def run_agent(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        rfis = json.load(file)

    with open(
        "data/haggett_all_rfis.json",
        "r",
        encoding="utf-8"
    ) as file:
        all_rfis = json.load(file)

    # The test set does not include creation dates.
    # Match each test RFI with the full Haggett Hall log.
    rfi_lookup = {
        str(item["rfi_id"]): item for item in all_rfis
    }

    results = []

    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as file:
            results = json.load(file)

    print(f"Loaded {len(rfis)} RFIs", flush=True)

    for rfi in rfis:
        rfi_id = str(rfi["rfi_id"])

        if rfi_id not in rfi_lookup:
            print(f"RFI #{rfi_id} not found in log")
            continue

        if any(
            str(result["rfi_id"]) == rfi_id
            for result in results
        ):
            print(
                f"Skipping RFI #{rfi_id} (already processed)",
                flush=True
            )
            continue

        # Use the complete original question.
        full_rfi = rfi_lookup[rfi_id]

        earlier_rfis = get_earlier_rfis(
            full_rfi,
            all_rfis
        )

        print(
            f"Analyzing RFI #{rfi_id}...",
            flush=True
        )

        try:
            result = triage_rfi(full_rfi, earlier_rfis)

            results.append(result)

            print(
                json.dumps(result, indent=2),
                flush=True
            )

        except Exception as e:
            print(
                f"RFI #{rfi_id} failed: {e}",
                flush=True
            )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(results, file, indent=2)

    print(
        f"Finished! {len(results)}/{len(rfis)} RFIs completed.",
        flush=True
    )


if __name__ == "__main__":
    runs = {
        "run1": (
            "data/rfi_test_set.json",
            "results/run1.json"
        ),
        "run2": (
            "data/rfi_test_set.json",
            "results/run2.json"
        ),
        "all35": (
            "data/haggett_all_rfis.json",
            "results/run_all35.json"
        )
    }

    if len(sys.argv) != 2 or sys.argv[1] not in runs:
        print("Usage: python agent/triage_agent.py run1")
        print("       python agent/triage_agent.py run2")
        print("       python agent/triage_agent.py all35")
        sys.exit(1)

    input_file, output_file = runs[sys.argv[1]]

    os.makedirs("results", exist_ok=True)

    run_agent(input_file, output_file)
