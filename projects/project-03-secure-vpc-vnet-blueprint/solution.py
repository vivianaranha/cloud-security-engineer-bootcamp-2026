"""Project 03: Secure VPC/VNet Blueprint."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.network import exposure_findings
def main(): print(exposure_findings({"source":"0.0.0.0/0","port":22}))

if __name__=='__main__':main()
