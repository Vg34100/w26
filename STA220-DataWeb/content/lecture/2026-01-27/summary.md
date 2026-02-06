# STA220-DATA | W04-Tue | 2026-01-27

## Action Items

- Remind the three students who haven’t registered their group yet
- Upload the five‑page project guideline document (includes abstract, intro, methods, results, references)
- Draft a concise abstract and motivation for your final project
- Choose a clear research question and list data sources (CSV files, APIs, web‑scraping)
- Set up a GitHub repo for the project and push initial code
- Install the requests and pandas packages; test CSV‑to‑SQL workflow

## Announcements

- February 6 deadline for upcoming weeks’ tasks
- Most students have registered groups; a few still need reminders
- Reminder to consult the SQL database report for reference

## Database Basics

- Use SELECT \* FROM table WHERE country='Austria' as a simple query template
- Parameterize queries with placeholders to avoid injection risks
- Drop and recreate tables only after confirming backups exist
- Load CSV data into a Pandas DataFrame, then export to SQL with to_sql
- Three ways to create a DB: direct SQL, CSV import, or Pandas‑driven upload

## SQL Injection Warning

- Direct string concatenation (... WHERE name='...') can be exploited
- Always use prepared statements or parameter placeholders

## Using CSV with Pandas

- Read CSV: df = pd.read_csv('file.csv')
- Export to DB: df.to_sql('table_name', con, if_exists='replace')
- Convert DB back to DataFrame with pd.read_sql_query
- Minimal code needed: three SQL statements for full round‑trip

## Web Scraping & APIs

- Two main approaches: HTML scraping (e.g., Wikipedia) vs. official APIs (REST)
- Respect rate limits: typically 1 request per second or per API policy
- Build query strings with ?param1=value1&param2=value2
- Use requests.get(url, params={...}) for clean parameter handling
- Cache responses to avoid duplicate requests and reduce load

## HTTP Status Codes & Requests

- 200 OK → request succeeded, but may need to parse response body
- 400‑series → client errors (e.g., bad request, unauthorized)
- 500‑series → server errors, retry later
- Cache headers can cause repeated identical responses; watch for stale data

## Project Guidelines & Deliverables

- Project must answer a specific research question or exploratory analysis
- Include: abstract, introduction, methods (SQL, pandas, scraping), results, visualizations, references
- Use at most three to five CSV files; store data in a relational DB if convenient
- Visualize key findings (charts, tables) rather than dumping full datasets
- Keep code modular; document API keys and credentials securely

## Tools & Packages

- pandas for data manipulation and CSV‑SQL conversion
- requests for HTTP calls and API interaction
- SQL client/library (e.g., sqlite3, SQLAlchemy) for database operations
- Optional: beautifulsoup4 for HTML scraping, json for API responses
- Version control with GitHub for collaboration and portfolio building
