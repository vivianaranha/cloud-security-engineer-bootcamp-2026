"""Project 02: Cloud IAM Least-Privilege Analyzer."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.iam import findings
def main(): print(findings({"actions":["*"],"mfa_required":False,"credential_type":"long_lived"}))

if __name__=='__main__':main()
