def recovery_ready(plan):
    required={"isolated_backup","restore_test","recovery_owner","rto","rpo"}
    present={k for k,v in plan.items() if v not in (None,False,"")}
    return {"ready":required<=present,"missing":sorted(required-present)}
