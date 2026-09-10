def storage_findings(item):
    f=[]
    if item.get("public"): f.append("public_storage")
    if not item.get("encrypted"): f.append("encryption_missing")
    if not item.get("logging"): f.append("access_logging_missing")
    return f
