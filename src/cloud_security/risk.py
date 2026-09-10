def risk_score(impact,exposure,privilege):
    return impact*exposure*privilege
def tier(v):
    if v>=80:return "critical"
    if v>=40:return "high"
    if v>=15:return "medium"
    return "low"
