def findings(role):
    out=[]
    actions=set(role.get("actions",[]))
    if "*" in actions: out.append("wildcard_action")
    if role.get("mfa_required") is False: out.append("mfa_not_required")
    if role.get("credential_type")=="long_lived": out.append("long_lived_credential")
    return out
