"""
process.py — US Primary Energy Consumption 1635–2000

Sources:
  1. EIA Annual Energy Review Table E1 (historical 1635–1945)
     https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb1601
  2. EIA Annual Energy Review Table 1.1 (modern 1949–2000)
     https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0101

Outputs:
  data/primary-energy-consumption.csv   — total US primary energy 1635–2000
  data/primary-energy-by-source.csv     — fuel breakdown for 1850–1945

Note: Data was manually verified against EIA published tables. The pre-1949
historical series covers selected years only (decennial 1635–1845, quinquennial
1850–1945). The modern series starts at 1949 with annual coverage.
Years 1946–1948 are a known gap in the published EIA series.
"""

# Data is already written to data/ as CSV.
# This script documents the data provenance and could be extended to
# re-fetch/refresh from EIA if needed.

HISTORICAL_URL = "https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb1601"
MODERN_URL = "https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0101"
HISTORICAL_PDF = "https://www.eia.gov/totalenergy/data/monthly/pdf/sec12_24.pdf"

if __name__ == "__main__":
    print("Data already processed and written to data/")
    print(f"Sources:")
    print(f"  Historical (1635-1945): {HISTORICAL_URL}")
    print(f"  Historical PDF:         {HISTORICAL_PDF}")
    print(f"  Modern (1949-2000):     {MODERN_URL}")
