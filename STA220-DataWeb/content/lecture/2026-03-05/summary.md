# STA220-DATA | W09-Thu | 2026-03-05

## Pet Adoption Data Project

- Shelters underfunded, databases messy, hard to search pets
- Goal: structured data → easier matching, higher adoption rates
- Scraped [rescueme.org](http://rescueme.org) listings (name, age, sex, compatibility, personality, health, urgent status, description, location)
- Built small getter functions → combined scraper per species → merged into one pandas DataFrame
- Compatibility categories: dogs, cats, kids (good / not good / unknown)
- Personality traits: energy (low‑avg‑high‑unknown) & temperament (sub‑avg‑dominant‑unknown)
- Visualized trait distributions with heat maps, highlighted top breeds & energy levels
- Modeling: linear regression + NLP on descriptions
  - NLP features: description length, top‑20 adjectives (TF‑IDF)
  - “Friendly” → slower adoption; “active”, “healthy”, “playful” → faster adoption
- Predictive model ranks pets by expected adoption speed
- Limitations: \~250 pets/species, only California, many unknown fields, possible inaccurate listings
- Extension ideas: swipe‑style matching app, partner with shelters to improve data entry

## Q&A – Pet Project

- Compatibility percentages derived from bullet‑point text on site (good vs not good)
- Blank compatibility fields → marked unknown
- Data limited to California to keep computation manageable; plan to scale with more resources

## Environmental Burden in California

- Data sources: CalEnviroScreen 2014, 2019, 2021 + EPA AQS PM2.5 & ozone (2019‑2021)
- Core questions: trend over decade, county vs national comparison, CES vs measured pollutants, hotspot concentration shifts
- Cleaned & aligned columns across years; created unified CSV for analysis
- Visuals: histograms, line graphs (time trends), choropleth & heat maps (spatial patterns), scatter plots (CES vs pollutants)
- Track‑level change: wide range (‑25 to +35); LA county most improved; 19 counties consistently up, 3 down
- North vs South: north shows steadier improvement
- Share metric: central‑valley counties (Merced, Fresno, Imperial, Tulare) high share of burden across years
- Validation: moderate positive correlation between CES and PM2.5 / ozone → supports CES as proxy
- Per‑capita comparison: Riverside, Orange County, San Diego rank high; LA appears lower per capita due to huge population
- Limitations: CES version changes, county averages mask intra‑county inequities, analysis descriptive not causal, still building full pipeline

## Q&A – Environmental Project

- Years chosen because CalEnviroScreen releases data every few years (2014, 2019, 2021)
- LMER models planned to assess pollutant predictors (PM2.5, ozone)
- Data gaps: e.g., NY county lacked air‑monitor data → excluded from analysis

## Film Industry Budget Analysis

- Focus: budget vs revenue disparity across production companies (2023 releases)
- Data prep: split comma‑separated genre columns, filter out zero/very low budgets (&lt; $10k)
- Top spenders: Paramount, Universal, Disney, Warner Bros; sharp drop after leading few companies
- Revenue vs budget scatter: overall positive trend, many films profitable
- Streaming releases cause missing budget/revenue entries in database
- Limitations: subsidiaries listed separately → double‑counting, budget breakdown opaque, streaming data incomplete

## Q&A – Film Project

- Data source: media database (publicly released budget/revenue figures)
- Handling missing values: set lower budget threshold, treat streaming‑only titles as unknown
- Acknowledged need to reconcile subsidiary companies for clearer spending picture.
