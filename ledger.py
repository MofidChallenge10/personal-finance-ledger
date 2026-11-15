"""CSV transaction summaries; input columns: date,description,amount,category."""
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

def summarize(path: Path) -> dict:
    totals=defaultdict(Decimal); count=0
    with path.open(newline="",encoding="utf-8-sig") as f:
        reader=csv.DictReader(f)
        required={"date","description","amount","category"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"CSV must include columns: {', '.join(sorted(required))}")
        for row in reader:
            try: amount=Decimal(row["amount"])
            except InvalidOperation as exc: raise ValueError(f"Invalid amount: {row['amount']}") from exc
            totals[row["category"].strip() or "Uncategorized"] += amount
            count += 1
    return {"transactions":count,"by_category":dict(sorted(totals.items())),
            "net":sum(totals.values(),Decimal("0"))}
def main():
    import argparse, json
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("csv_file",type=Path); a=p.parse_args()
    result=summarize(a.csv_file)
    print(json.dumps({k:({x:str(y) for x,y in v.items()} if isinstance(v,dict) else str(v) if k=="net" else v) for k,v in result.items()},indent=2))
if __name__=="__main__": main()
