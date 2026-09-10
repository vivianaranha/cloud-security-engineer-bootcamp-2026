def posture_score(checks):
    if not checks:return 1.0
    return sum(bool(v) for v in checks.values())/len(checks)
def failed_controls(checks): return sorted(k for k,v in checks.items() if not v)
