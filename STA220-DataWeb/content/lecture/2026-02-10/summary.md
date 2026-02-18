# STA220-DATA | W06-Tue | 2026-02-10

## Action Items

- Run the code locally; verify the uploaded file from this morning is present
- Set up a daily upload of the algorithm to keep data current
- Install required Python packages (e.g., astral, geopy)
- Combine timestamps into a comma‑separated string for a single API call
- Add the footprint column and filter rows where distance &lt; footprint
- Cross‑check visibility results with the issage website and note any mismatches
- Refine the Selenium script: headless mode, custom window size, explicit waits, screenshot on error

## Project Overview

- Goal: determine when the ISS is visible from Davis, CA
- Workflow: fetch sunrise/sunset, build time windows, query ISS position API, compute visibility
- Data sources: astronomical package for dawn/dusk, ISS position API, external issage site for validation

## Time Handling & Conversion

- Two time formats encountered; converted both to Python datetime objects
- Also transformed times to seconds‑since‑epoch for easy arithmetic
- Adjusted for an 8‑hour offset when comparing local and UTC times
- Current reference date used: February 10 (example in code)

## Sunrise/Sunset & Visibility Window

- Used astral (or similar) to get dawn and dusk for the target location
- Defined a 75‑minute buffer before dawn and after dusk
- Created a 90‑minute window with 10‑second steps (≈ 9 000 timestamps)
- Planned to check ISS position at each step to see if it falls within the visible sky

## API Request Optimization

- API docs allow multiple timestamps per request (comma‑separated)
- Built a list of timestamps, joined with commas, and passed to the get_positions endpoint
- Reduced \~4 000 separate requests to a handful of batched calls
- Added a progress bar; estimated total run time ≈ 7 minutes

## ISS Visibility Table & Footprint Analysis

- Generated a DataFrame with timestamp, latitude, longitude, distance, and footprint radius
- Dropped irrelevant columns (altitude, constant visibility flag) to keep table tidy
- Added footprint column based on ISS altitude and observer’s horizon
- Filtered rows where distance &lt; footprint; found \~280 moments of visibility

## Direction & Angle Calculation

- Computed bearing from Davis to ISS projection using latitude/longitude pairs
- Converted bearing (0‑360°) to cardinal directions by dividing by 45 and rounding
- Example: 260° → “south‑west”, matching visual expectations from the map
- Verified direction output against known locations (e.g., San Francisco)

## Selenium Automation for Web Testing

- Set up Chrome WebDriver (headless option for background runs)
- Implemented explicit waits (≈ 1‑2 seconds) before interacting with elements
- Maximized or resized window to avoid bot detection (avoid default 600×800 size)
- Captured screenshots on exceptions for debugging
- Demonstrated element location strategies: id, xpath, css selector
- Showed form‑filling workflow (first name, gender, favorite color) and page navigation (scroll, refresh)
- Emphasized rate‑limit awareness: throttle requests, reuse sessions, handle bans gracefully
