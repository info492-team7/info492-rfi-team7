
# RFI Triage Agent - GC Team 7

def triage_rfi(rfi):
    result = {
        "rfi_id": rfi["rfi_id"],
        "needs_response": True,
        "root_cause": None,
        "responder": None,
        "due": None,
        "contractual_risk": None,
        "risk_reason": None,
        "priority": None,
        "duplicate_of": None
    }

    return result

# Test with a sample RFI
if __name__ == "__main__":
    import json

    sample_rfi = {
        "rfi_id": 48,
        "question": "Please clarify whether bid options 1-5 are adds or deducts."
    }

    result = triage_rfi(sample_rfi)
    print(json.dumps(result, indent=2))
