MAP={
"identity":{"aws":"IAM / IAM Identity Center","azure":"Microsoft Entra ID / Azure RBAC","gcp":"Cloud IAM"},
"keys":{"aws":"AWS KMS","azure":"Azure Key Vault","gcp":"Cloud KMS"},
"secrets":{"aws":"AWS Secrets Manager","azure":"Azure Key Vault","gcp":"Secret Manager"},
"audit":{"aws":"AWS CloudTrail","azure":"Azure Activity Log","gcp":"Cloud Audit Logs"},
"security_posture":{"aws":"AWS Security Hub","azure":"Microsoft Defender for Cloud","gcp":"Security Command Center"},
}
def service_map(capability): return MAP[capability]
