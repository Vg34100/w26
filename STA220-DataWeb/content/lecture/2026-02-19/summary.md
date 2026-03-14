# STA220-DATA | W07-Thu | 2026-02-19

## Action Items

- Finish choropleth map for ecological footprint (calc max, merge GeoJSON, set colors)
- Add validation for the get_book_type (or similar) function
- Incorporate air‑quality API data per notes in the shared doc
- Contact Jordan about the linguistics project option
- Join the Discord group (username scott_heather_c) and confirm access
- Clean up preprocessing: drop irrelevant columns, rename fields, handle null rows

## Main Concepts

- Choropleth maps = colored regions, easier to read than long tables
- Need two inputs: geographic shapes (GeoJSON) + numeric data (CSV)
- Use address‑to‑coordinates package for point markers on the map
- Color scale: low = green, medium = yellow, high = red (can reverse)
- Adjust opacity and add layer control for better readability

## Data Sources & Preparation

- Ecological footprint CSV: per‑capita footprint, biocapacity, etc.
- Country borders GeoJSON: includes name, abbreviation, polygon geometry
- US unemployment data keyed by state abbreviations
- UK election results scraped from Wikipedia tables, then cleaned
- Drop unused columns, rename for consistency, move first null row

## Technical Steps (Folium/Mapping)

- Init map with tile layer (e.g., OpenStreetMap)
- Add GeoJSON layer, link data via key_on (e.g., [properties.name](http://properties.name))
- Define style_function using get_color based on data value
- Create separate FeatureGroup for each metric/party
- Add pop‑ups showing region name and value
- Insert LayerControl to toggle layers, set opacity (≈0.8)

## Example Visualizations Discussed

- World map of ecological footprint (dark red = high, dark green = low)
- US map of unemployment rates by state (color intensity per rate)
- UK constituency map showing vote share for four major parties
- Climate‑crisis data set map combining footprint and biocapacity

## Challenges & Tips

- Ensure key fields match between data frame and GeoJSON (name vs abbreviation)
- Complex polygons can be large; store GeoJSON locally or on a server
- Missing data → white regions; verify both datasets cover same areas
- Reverse palette by adding \_r to the color name
- Use linear color map for smooth shading across value range
