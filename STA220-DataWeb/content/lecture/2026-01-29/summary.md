# STA220-DATA | W04-Thu | 2026-01-29

## Action Items

- Install requests and requests‑cache (or similar) in your notebook
- Write a function to build the POST payload from the copied network parameters
- Add a 1‑second time.sleep between requests to respect rate limits
- Export the collected JSON rows into a pandas DataFrame and save as CSV
- Try the same workflow on the health‑inspection site (search by county, loop pages)

## Overview of Undocumented APIs

- Often hidden behind the web page’s JavaScript, not listed in public docs
- Can be discovered by inspecting network traffic while using the site
- Usually return JSON with the data you need (e.g., salaries, inspection scores)
- Access may require an API key or authentication token – keep it private

## Finding APIs via Browser DevTools

- Open Chrome/Firefox DevTools → **Network** tab
- Perform the action on the site (search, filter, paginate)
- Look for XHR/fetch entries that return application/json
- Click the request → **Headers** → copy **Request URL**, **Method**, **Payload** and **Headers** (User‑Agent, Authorization, etc.)
- Note pagination parameters (page, count, offset) and any filters (location=all, sidx=personal)

## Building and Sending Requests

- Replicate the captured request with requests.post(url, json=payload, headers=headers)
- Include required auth token/key in the header (Authorization: Bearer &lt;key&gt;)
- Adjust pagination values to loop through all pages (e.g., page=1…7)
- Respect server limits: **≤ 1 request per second** (or as indicated by the site)

## Data Extraction & Processing

- Parse the JSON response → focus on the rows array (each row = one record)
- Convert rows to a pandas DataFrame (pd.DataFrame(rows))
- Cast date strings to pd.Timestamp for easy time‑series analysis
- Add derived columns (e.g., day_name = timestamp.dt.day_name())
- Combine results from all pages into a single tidy DataFrame

## Example: Newspaper Articles (Election Week)

- Goal: fetch \~300 articles, limit to first 15 per page (max 50)
- Loop through pages, collect article titles, dates, sources
- Analyze publication frequency by day of week, compare candidates (e.g., Harris vs. Biden)
- Visualize counts with a simple bar chart

## Example: California Health Inspections

- Site provides inspection data via hidden POST API (search by county, date range)
- Required parameters: tab=0, count=25, dateFrom=2024-01-01, dateTo=2024-01-31
- Each restaurant has a private inspectionId; fetch all scores by looping over IDs
- Many scores are null or 0; switch to counties with non‑zero values for richer analysis
- Build a map or dashboard showing inspection scores per location

## Tips & Best Practices

- Always check the response size; limit rows per request to avoid timeouts
- Cache repeated requests during development to speed up debugging
- Never share your API key publicly; store it in environment variables or a .env file
- Monitor for HTTP errors (403, 429) and back‑off accordingly
- Document the exact request parameters and headers for reproducibility

---

*End of notes.*
