"""Project 14: Multi-Cloud Security Control Plane."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.mapping import service_map
def main():
 for c in ["identity","keys","secrets","audit","security_posture"]:print(c,service_map(c))

if __name__=='__main__':main()
