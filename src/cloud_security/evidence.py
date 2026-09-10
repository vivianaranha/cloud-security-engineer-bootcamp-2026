def evidence_status(control):
    required=set(control.get("required_evidence",[])); present=set(control.get("present_evidence",[]))
    return {"complete":required<=present,"missing":sorted(required-present)}
