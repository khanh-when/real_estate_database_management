# Project Xero

## I. MariaDB Setup

- MariaDB is used as the backing store for historical stock and ETF price data.
- CSV sources:
  - `archive/stocks/`
  - `archive/etfs/`
- Tables store:
  - Stock metadata (tickers, names, categories, ETF flag)
  - Daily price data (date, open, high, low, adjusted close, volume)

---

## II. ETL Pipeline (Extract → Transform → Load)

### 1. Extract
- Read raw `.csv` files using glob patterns (e.g. `archive/stocks/*.csv`).
- Parse each file into in-memory Python structures.

### 2. Filter
- Skip clearly bad or irrelevant rows.
- Currently:
  - Only accept data from **year 2000 and later**.
  - Skip rows with invalid fields.

### 3. Transform
- Convert each CSV row into a normalized structure:
  - Dates → `DATE` objects.
  - Price fields → rounded floats (2 decimal places).
  - Volume → integers.
- Detect corrupted values, such as:
  - `OpenPrice = 0.0` with nonsensical `AdjClosePrice` (e.g., `-1e21`).
- Store cleaned data in:
  - Nested dictionaries for lookup.
  - `list[tuple]` structures for bulk insertion.

### 4. Load
- Use `executemany` to insert into MariaDB in **batches**.
- The loader runs in a loop over chunks of data instead of a single huge insert.

---

## III. Issues & Troubleshooting

### 1. Data Quality Problems
- Errors seen:
  - `Out of range value for column '...' at row (...)`
- Root causes:
  - Corrupted historical rows (e.g., absurd negative adjusted close values in the 1980s).
  - Some rows with invalid or extreme numeric values.
- Mitigation:
  - Filter out pre-2000 data.
  - Skip rows with
