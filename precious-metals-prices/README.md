# Precious Metals Prices

Monthly price series for silver, platinum, and palladium in USD per troy ounce, 1968–present. Complements the [gold-prices](https://github.com/datasets/gold-prices) dataset.

Each metal has an [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code:

| Metal | ISO 4217 | Coverage | Rows |
|-------|----------|----------|------|
| Silver | XAG | 1968–present | ~699 |
| Platinum | XPT | 1968–present | ~697 |
| Palladium | XPD | 1968–present | ~699 |

## Data

### `silver.csv`
Monthly silver prices in **USD per troy ounce** (XAG/USD), month-end closing prices.

| Field | Description |
|---|---|
| `date` | Last calendar day of the month (YYYY-MM-DD) |
| `price` | Silver price in USD per troy ounce |

### `platinum.csv`
Monthly platinum prices in **USD per troy ounce** (XPT/USD), month-end closing prices.

| Field | Description |
|---|---|
| `date` | Last calendar day of the month (YYYY-MM-DD) |
| `price` | Platinum price in USD per troy ounce |

### `palladium.csv`
Monthly palladium prices in **USD per troy ounce** (XPD/USD), month-end closing prices.

| Field | Description |
|---|---|
| `date` | Last calendar day of the month (YYYY-MM-DD) |
| `price` | Palladium price in USD per troy ounce |

## Source

Data sourced from [Stooq](https://stooq.com) (XAG/USD, XPT/USD, XPD/USD monthly series), which aggregates London fix and spot market data.

## License

Public domain — [ODC PDDL](https://opendatacommons.org/licenses/pddl/1.0/).
