# CYM SESSION 2 - Discussion with Cadillac Bob

## Action Items
- Review Prof. Blumenstock’s Rwanda phone‑log study (856 surveyed users → 1.5 M predictions)  
- Practice building a deterministic‑finite‑automata feature generator for call‑detail records  
- Compare wealth‑prediction maps with national statistics (correlation ≈ 0.92)  
- Explore bias‑mitigation techniques (e.g., exclude gender, ethnicity, income variables)  
- Draft a short proposal on using mobile‑phone data for real‑time disaster monitoring  

## Overview
- “Data‑intensive international development” = using new digital traces to fight poverty  
- Traditional surveys are scarce, expensive, and often outdated in low‑income countries  
- Mobile‑phone logs and satellite imagery are the two abundant data sources in many developing regions  

## Data Sources & Challenges
- Mobile‑phone operators log every call, SMS, and tower location (metadata) for billing  
- Census gaps: Madagascar 21 yr, Afghanistan 35 yr, Angola 44 yr between full censuses  
- Digital divide: phone ownership skewed by gender, income, education → biased footprint  
- Bandwidth linked to income → persistent representation bias even as connectivity spreads  

## Feature Engineering & Machine Learning
- Raw call‑detail records → thousands of quantitative “features” (calls/day, unique towers, SMS entropy)  
- Deterministic finite‑state automaton automatically generates tens of thousands of metrics  
- Supervised learning: inputs = phone features, output = survey‑measured wealth (label)  
- Model learns mapping, identifies most predictive features (e.g., weighted average of first‑degree neighbors’ day‑of‑week SMS entropy)  

## Key Findings (Rwanda Case)
- 856 surveyed users provided ground‑truth wealth and phone‑log features  
- Ratio of outgoing → incoming calls *does* correlate with wealth, but not the strongest predictor  
- Top predictive feature: weighted average of neighbors’ day‑of‑week SMS‑volume entropy  
- Model applied to 1.5 M Rwandan users → high‑resolution wealth map (≈ 21 00 cells)  
- Map correlates 0.92 with national institute’s district‑level wealth estimates  

## Applications & Implications
- Fine‑grained poverty maps enable targeted aid, road/health‑facility planning, and rapid crisis response  
- Real‑time monitoring: phone‑traffic spikes during the 2008 Kivu earthquake revealed affected regions within minutes  
- Potential for “predictive policing,” insurance pricing, and political micro‑targeting (ethical red flags)  
- Cost comparison: traditional household survey ≈ $10 M, phone‑data approach ≈ $15–20 k for a two‑month rollout  

## Limitations & Ethical Concerns
- **Bias**: data reflect existing socioeconomic and gender disparities; models can inherit discrimination  
- **Misinterpretation**: correlation ≠ causation; spurious links (e.g., shoe size ↔ Internet use) can mislead  
- **Privacy**: metadata can re‑identify individuals; misuse in surveillance or “filter bubbles”  
- **Lucas critique**: policy changes alter underlying behavior, breaking model assumptions over time  
- **Stationarity**: behavior patterns shift (e.g., Google Flu Trends failed after 2013) → models lose predictive power  

## Opportunities & Future Directions
- Combine mobile data with satellite, weather, and agricultural datasets for climate‑impact studies  
- Develop open‑source pipelines for feature generation and bias‑mitigation (e.g., fairness‑constrained trees)  
- Use simulations (e.g., SimCity‑style) calibrated with big data to explore “what‑if” policy scenarios  
- Foster cross‑sector partnerships (academia ↔ industry ↔ aid agencies) to build shared data infrastructure  
- Train the next generation of data scientists in low‑resource settings (fellowships, curricula).
