# Personal Finance Ledger
Summarize transactions from a CSV file using decimal arithmetic to avoid floating-point money errors.

## CSV format
Required columns: `date,description,amount,category`. Use negative amounts for expenses and positive amounts for income.

## Run
```bash
python ledger.py transactions.csv
python -m unittest discover -s tests -v
```

The report includes transaction count, net balance, and totals by category. It performs local processing only and does not connect to banks or provide financial advice.
