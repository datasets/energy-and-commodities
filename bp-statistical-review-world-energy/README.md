# BP Statistical Review of World Energy

Annual flagship energy statistics covering production, consumption, and prices by country and fuel type. Based on the BP Statistical Review of World Energy 2020 (69th edition), with data through 2019.

## Background

The BP Statistical Review of World Energy is one of the most widely cited sources of global energy data. Published annually since 1952, it covers oil, gas, coal, nuclear, hydro, and renewables across 60+ countries and regions, alongside price series for crude oil, natural gas, and coal going back to the 1970s and 1980s.

## Data

All files are in `data/` in long format (one row per country per year), except the price files which are wide format (one row per year, one column per benchmark).

### Production and Consumption

| File | Description | Coverage |
|------|-------------|----------|
| `primary-energy-consumption.csv` | Total primary energy consumption, all sources (EJ) | 1965–2019 |
| `oil-production.csv` | Crude oil and NGL production (thousands of barrels per day) | 1965–2019 |
| `oil-consumption.csv` | Oil consumption (thousands of barrels per day) | 1965–2019 |
| `gas-production.csv` | Natural gas production (Bcm) | 1970–2019 |
| `gas-consumption.csv` | Natural gas consumption (Bcm) | 1965–2019 |
| `coal-production.csv` | Coal production (million tonnes) | 1981–2019 |
| `coal-consumption.csv` | Coal consumption (EJ) | 1965–2019 |
| `nuclear-generation.csv` | Nuclear electricity generation (TWh) | 1965–2019 |
| `hydro-generation.csv` | Hydroelectric generation (TWh) | 1965–2019 |
| `renewables-consumption.csv` | Wind, solar, geothermal, biomass consumption (EJ, excludes hydro) | 1965–2019 |
| `co2-emissions.csv` | CO2 emissions from energy use (million tonnes) | 1965–2019 |

### Prices

| File | Description | Coverage |
|------|-------------|----------|
| `oil-spot-prices.csv` | Annual average spot prices for Dubai, Brent, Nigerian Forcados, and WTI (USD per barrel) | 1972–2019 |
| `gas-prices.csv` | Annual average prices at Japan LNG CIF, JKM, German import, UK NBP, Netherlands TTF, and US Henry Hub (USD per million Btu) | 1984–2019 |
| `coal-prices.csv` | Annual average prices at Northwest Europe, US Appalachian, Japan steam CIF, China Qinhuangdao, and Japan coking CIF (USD per tonne) | 1987–2019 |

## Sources

- BP. [Statistical Review of World Energy 2020](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html). 69th edition.

## Reproduce

```bash
python3 process.py
```

## License

Free to use with attribution to BP Statistical Review of World Energy.
