# CMN SESSION 6 - Social Network Analysis 2

## Action Items

- Review the **fusion‑networks** review paper ([socialdynamics.org](http://socialdynamics.org))
- Watch the **Nicolas Krispakis & James Fowler** video on the Framingham Heart Study network evolution
- Run a few **NetLogo** simulations of random, scale‑free and small‑world networks
- Practice calculating **training vs. test sets** for predictive models on social‑media data
- Summarize the professor’s “four common network constellations” in your own words

## Influencer Myth vs. Reality

- Celebrities (e.g., Kim Kardashian, LeBron James) command high fees—≈ $10 k per tweet
- Top‑retweeted tweets are often from famous accounts, but many viral posts come from ordinary users
- Empirical data shows **98 % of tweeted links never get reposted**; a tiny fraction go viral
- The probability a tweet goes viral **given** it’s from an influencer is low (base‑rate fallacy)
- Influencers act more like **mass‑media broadcasters**: they reach many people directly, increasing odds that some will further share

## Empirical Twitter Study

- Tracked **74 M URLs** posted by **1.6 M users** over two months (2009)
- Used **shortened URLs** to follow exact repost chains (each short link is unique)
- Found a **power‑law‑like distribution** of repost counts: most links get 0–1 reposts, a few get thousands
- Only two variables significantly predicted future influence: **follower count** and **past cascade success**
- Model fit was poor → many unobserved factors drive virality

## Base‑Rate Fallacy & Bayes’ Rule

- Example: a rare disease (≈ 1 in 6 M) vs. common symptoms (1 in 3) → probability of disease given symptoms ≈ 1 in 2 M
- People often confuse **P(symptoms | disease)** (≈ 100 %) with **P(disease | symptoms)** (very low)
- Same error appears when judging influencer impact: high **P(influencer | viral)** but low **P(viral | influencer)**

## Network Models Overview

- **Random (Erdős–Rényi) graphs**: links formed uniformly at random; useful as statistical baselines
- **Scale‑free (preferential‑attachment) networks**: “rich‑get‑richer” → power‑law degree distribution
- **Small‑world networks**: high clustering + short average path length (≈ 6 degrees of separation)
- **Hybrid models**: mix random linking, preferential attachment, and geographic proximity

## Random Networks & Giant Component

- Average degree ⟨k⟩ ≈ (p × (n − 1)) where *p* is link probability, *n* nodes
- **Threshold at ⟨k⟩ ≈ 1**: below this, components stay tiny; above it, a **giant component** rapidly emerges
- Simulations with 50 nodes showed the giant component growing from 0 % to \~16 % once the average degree passed 1

## Scale‑Free Networks & Preferential Attachment

- New nodes attach to existing nodes with probability proportional to current degree → few hubs, many leaves
- Hubs dramatically speed up diffusion (e.g., disease, rumors) because they connect to many others
- Power‑law degree distribution: **exponentially few nodes have exponentially many links**

## Small‑World Networks

- Combine **high clustering** (tight local groups) with **short global paths** (quick reach across the network)
- Rewiring a regular lattice introduces “shortcuts” that lower average path length while preserving clustering up to a point
- Real‑world examples: social circles, airline hubs, the “six degrees of separation” phenomenon

## Cost‑Benefit Model of Network Formation

- Links provide **benefits** (access to information, resources) and incur **costs** (time, effort)
- Extreme cases:
  - **Zero cost** → fully connected **clique** is optimal
  - **Very high cost** → empty network (no links) is optimal
- **Intermediate costs** → **star network** maximizes total benefit while minimizing total cost

## Stability vs. Efficiency

- **Social efficiency**: maximize sum of net benefits across all nodes
- **Social stability**: no individual can improve payoff by adding/removing a link (pairwise stable equilibrium)
- Star networks are efficient but **unstable**: the central hub bears high costs, peripheral nodes benefit more
- Stabilization requires **subsidies/tax transfers** from peripherals to the hub (or external funding) to equalize payoffs

## Intervention Strategies (Vaccination Example)

- Random vaccination is inefficient in scale‑free networks; targeting **high‑degree hubs** breaks transmission chains quickly
- Practical proxy: ask people to name friends, then vaccinate those friends (friends of random respondents tend to be well‑connected)

## Key Take‑aways

- Influencer marketing is not a guaranteed shortcut; network structure matters more than individual fame
- Empirical Twitter data shows **high variability** in cascade success; most content never spreads
- Understanding **base rates** prevents over‑estimating influencer impact
- Different network topologies produce distinct diffusion dynamics; simulations help reveal these effects
- Designing **stable and efficient** networks often requires **external incentives** (taxes, subsidies) to balance individual costs

---

*Prepared for Pablo, a student following Prof. Lamberson’s lecture on computational social science and network analysis.*
