"""Project 18: Cloud GRC Evidence Pack."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.evidence import evidence_status
def main(): print(evidence_status({"required_evidence":["policy","log","test"],"present_evidence":["policy","log"]}))

if __name__=='__main__':main()
