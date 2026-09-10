import sys,unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from cloud_security.iam import findings
from cloud_security.network import exposure_findings
from cloud_security.storage import storage_findings
from cloud_security.posture import posture_score,failed_controls
from cloud_security.risk import risk_score,tier
from cloud_security.evidence import evidence_status
from cloud_security.resilience import recovery_ready
from cloud_security.mapping import service_map
class T(unittest.TestCase):
 def test_iam(self): self.assertEqual(len(findings({"actions":["*"],"mfa_required":False,"credential_type":"long_lived"})),3)
 def test_network(self): self.assertIn("public_admin_port",exposure_findings({"source":"0.0.0.0/0","port":22}))
 def test_storage(self): self.assertEqual(len(storage_findings({"public":True,"encrypted":False,"logging":False})),3)
 def test_posture(self): self.assertEqual(posture_score({"a":True,"b":False}),.5);self.assertEqual(failed_controls({"a":True,"b":False}),["b"])
 def test_risk(self): self.assertEqual(risk_score(5,5,4),100);self.assertEqual(tier(100),"critical")
 def test_evidence(self): self.assertFalse(evidence_status({"required_evidence":["a","b"],"present_evidence":["a"]})["complete"])
 def test_recovery(self): self.assertTrue(recovery_ready({"isolated_backup":True,"restore_test":True,"recovery_owner":"x","rto":4,"rpo":1})["ready"])
 def test_map(self): self.assertIn("CloudTrail",service_map("audit")["aws"])
if __name__=="__main__":unittest.main()
