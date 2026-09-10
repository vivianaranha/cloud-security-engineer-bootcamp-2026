"""Project 06: Cloud Posture Dashboard."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from cloud_security.posture import posture_score,failed_controls
def main():
 c={"mfa":True,"logging":True,"public_storage_blocked":False};print(posture_score(c),failed_controls(c))

if __name__=='__main__':main()
