def exposure_findings(rule):
    f=[]
    if rule.get("source") in ("0.0.0.0/0","::/0") and rule.get("port") in (22,3389): f.append("public_admin_port")
    if rule.get("source") in ("0.0.0.0/0","::/0") and rule.get("sensitive_backend"): f.append("public_sensitive_backend")
    return f
