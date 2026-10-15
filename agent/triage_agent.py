
# RFI Triage Agent - GC Team 7

import json
from google import genai
from google.genai import types

client = genai.Client()

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
- priority (low, medium, or high)
- duplicate_of (null if unknown)

Consider project cost, schedule, safety, and
contractual impact when assigning priority.
Use null if information cannot be determined.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        )
    )

    return json.loads(response.text)


if __name__ == "__main__":
    sample_rfi = {
        "rfi_id": 48,
        "question": "Please clarify whether bid options 1-5 are adds or deducts."
    }

    result = triage_rfi(sample_rfi)
    print(json.dumps(result, indent=2))
