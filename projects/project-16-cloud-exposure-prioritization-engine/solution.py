"""Project 16: Cloud Exposure Prioritization Engine."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.risk import risk_score,tier
def main():
 s=risk_score(5,5,4);print(s,tier(s))

if __name__=='__main__':main()
