"""
Process precious metals price data from Stooq into clean monthly CSVs.

Sources:
  Silver (XAG/USD):   https://stooq.com/q/d/l/?s=xagusd&i=m
  Platinum (XPT/USD): https://stooq.com/q/d/l/?s=xptusd&i=m
  Palladium (XPD/USD): https://stooq.com/q/d/l/?s=xpdusd&i=m

Outputs:
  data/silver.csv    — monthly silver prices, USD/troy oz, 1968–present
  data/platinum.csv  — monthly platinum prices, USD/troy oz, 1968–present
  data/palladium.csv — monthly palladium prices, USD/troy oz, 1968–present

Prices are month-end closing prices (London fix / spot). All metals priced
in USD per troy ounce.
"""

import csv
import urllib.request
from datetime import datetime

METALS = [
    {
        "id": "silver",
        "symbol": "xagusd",
        "name": "Silver",
        "iso4217": "XAG",
    },
    {
        "id": "platinum",
        "symbol": "xptusd",
        "name": "Platinum",
        "iso4217": "XPT",
    },
    {
        "id": "palladium",
        "symbol": "xpdusd",
        "name": "Palladium",
        "iso4217": "XPD",
    },
]

START_DATE = datetime(1968, 1, 1)  # consistent start across all three metals


def fetch_stooq(symbol: str) -> list[dict]:
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=m"
    print(f"  Fetching {url}")
    with urllib.request.urlopen(url) as resp:
        lines = resp.read().decode("utf-8").splitlines()
    reader = csv.DictReader(lines)
    return list(reader)


def process_metal(metal: dict) -> None:
    rows = fetch_stooq(metal["symbol"])

    out_path = f"data/{metal['id']}.csv"
    count = 0
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "price"])
        for row in rows:
            date = datetime.strptime(row["Date"], "%Y-%m-%d")
            if date < START_DATE:
                continue
            price = float(row["Close"])
            writer.writerow([row["Date"], f"{price:.4f}"])
            count += 1

    print(f"  {out_path}: {count} rows")


if __name__ == "__main__":
    for metal in METALS:
        print(f"Processing {metal['name']} ({metal['iso4217']})...")
        process_metal(metal)
    print("Done.")
