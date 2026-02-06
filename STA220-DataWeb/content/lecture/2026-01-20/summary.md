# STA220-DATA | W03-Tue | 2026-01-20

## Action Items

- Close SQLite connection after queries
- Use pandas.read_sql() for quick DataFrame loading
- Apply multiprocessing only for CPU‑bound tasks (avoid when I/O‑bound)
- Standardize features before fitting linear regression
- Perform k‑fold cross‑validation to pick tuning parameter with lowest MSE

## House Price Modeling Overview

- Dataset includes census info: median income, house age, rooms, population, etc.
- Goal: predict house price (in hundreds of dollars)
- Target variable \~ $55,000 average price
- Features: median income, average rooms, households, etc.

## Cross‑Validation Procedure

- Split data into 10 folds (e.g., 20 000 rows)
- For each fold: train on 9 folds, test on the held‑out fold
- Compute MSE for each fold, then average across folds
- Choose tuning parameter that yields smallest average MSE

## Model Findings

- Median income → strong positive coefficient (richer areas cost more)
- House age → near‑zero effect, possibly insignificant
- Average bedrooms → positive impact (more bedrooms → higher price)
- Average rooms → unexpected negative effect (possible holiday‑home bias)
- Population → no clear effect
- Longitude & latitude → clear geographic price gradient (coastal areas pricier)

## SQL & SQLite Basics

- Convert CSV/Excel to SQLite DB for easier querying
- Connect with sqlite3.connect('path/to/db')
- Basic query: SELECT \* FROM table_name;
- Use PRAGMA table_info(table_name); to list columns

## Working with Olympic Games Data

- Two tables: summer and winter Olympic results
- Columns include year, host country, gold/silver/bronze counts, etc.
- Example query: SELECT year, host_country, gold FROM winter;

## SQL Query Techniques

- DISTINCT to list unique host countries
- ORDER BY gold DESC to rank most successful nations
- LIMIT 10 to view top rows quickly
- Combine columns for points: gold\*5 + silver\*2 + bronze\*1 AS points
- Filter with WHERE year &gt;= 2000 AND year &lt;= 2010
- Use IN for multiple host countries: WHERE host_country IN ('USA','JPN','KOR')
- Pattern matching with LIKE '%USA%'

## Tips & Best Practices

- Prefer pandas.read_sql() over manual cursor loops for speed and readability
- Always close DB connections to avoid “cannot operate on a closed database” errors
- When aggregating, place WHERE before GROUP BY; use HAVING for post‑aggregation filters
- For large datasets, consider indexing key columns (e.g., year, country)
- Keep SQL keywords uppercase for clarity (SELECT, FROM, WHERE, etc.)
