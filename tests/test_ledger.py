import tempfile, unittest
from pathlib import Path
from ledger import summarize
class LedgerTests(unittest.TestCase):
    def test_category_totals(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.csv"; p.write_text("date,description,amount,category\n2026-01-01,Coffee,-3.5,Food\n2026-01-02,Pay,10,Income\n")
            r=summarize(p); self.assertEqual(r["net"], __import__("decimal").Decimal("6.5")); self.assertEqual(r["transactions"],2)
    def test_missing_columns(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.csv"; p.write_text("date,amount\n2026-01-01,2\n")
            with self.assertRaises(ValueError): summarize(p)
if __name__=="__main__": unittest.main()
