
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
