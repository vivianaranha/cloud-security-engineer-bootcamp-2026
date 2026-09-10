"""Project 04: Cloud Data Protection Architecture."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.storage import storage_findings
def main(): print(storage_findings({"public":True,"encrypted":False,"logging":False}))

if __name__=='__main__':main()
