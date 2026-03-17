# US Primary Energy Consumption 1635–2000

Estimated primary energy consumption in the United States from 1635 to 2000. Covers 365 years of US energy history — from wood and water power in the colonial era, through the coal-dominated industrial revolution, to the rise of petroleum and natural gas in the 20th century.

## Data

| File | Description | Coverage |
|------|-------------|----------|
| `data/primary-energy-consumption.csv` | Total primary energy consumption | 1635–2000 |
| `data/primary-energy-by-source.csv` | Breakdown by fuel type | 1850–1945 (selected years) |

All values in **quadrillion Btu** (quad Btu). 1 quad Btu = 10¹⁵ Btu ≈ 1.055 exajoules.

### Coverage notes

- **1635–1845**: Decennial selected years. Colonial and early republic era — almost entirely wood fuel and water power.
- **1850–1945**: Quinquennial selected years. Covers the industrial revolution and rise of fossil fuels. Source breakdown available.
- **1946–1948**: Gap in published EIA series (bridge between historical and modern datasets).
- **1949–2000**: Annual data from EIA Monthly/Annual Energy Review. Full energy system including nuclear from ~1957.

## Key milestones

| Year | Event |
|------|-------|
| 1850 | Coal begins appearing in energy mix (0.219 quad) |
| 1880s | Natural gas first recorded |
| ~1900 | Coal surpasses wood as primary energy source |
| ~1950 | Petroleum surpasses coal |
| 1957 | Nuclear energy enters the grid |
| 1970 | Peak consumption growth era: 67.8 quad Btu |
| 1973–74 | Oil crisis: consumption falls from 75.7 to 74.0 quad Btu |
| 2000 | US consumes 98.8 quad Btu — the highest to that point |

## Sources

- **1635–1945**: EIA Annual Energy Review, Table E1 — *Estimated Primary Energy Consumption in the United States, Selected Years, 1635–1945*
  - Original source: USDA Circular No. 641 and *Energy in the American Economy, 1850–1975* (Schurr & Netschert)
  - EIA PDF: https://www.eia.gov/totalenergy/data/monthly/pdf/sec12_24.pdf

- **1949–2000**: EIA Annual Energy Review, Table 1.1 — *Primary Energy Overview*
  - https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0101

## License

US government data (EIA) — public domain. This packaged dataset is released under the [Open Data Commons Public Domain Dedication and License (PDDL)](https://opendatacommons.org/licenses/pddl/).
