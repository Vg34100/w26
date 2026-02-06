# ECS269 SE - 01/12 W2/M

## Action Items

- Find LaTeX template in LMS → Assignments → “Proposal” (download .tex, .cls, .bib).
- If template missing, email TA or post on class forum.
- Draft 2‑page proposal covering topic, RQs, theory, refs, method, timeline.
- Use single‑column, normal font size; avoid two‑column layout.
- Submit proposal by the 19th (extra‑day vote passed, no objections).
- Upload final file to shared group directory (optional but recommended).
- Incorporate validity/reliability discussion and threat‑to‑validity notes in proposal.

## Proposal Requirements

- 2‑page limit, required sections: topic, research questions, theoretical background, preliminary references, method, time‑phased plan.
- Optional LaTeX template; follow provided .tex file if used.
- Single column, normal font size; no shrinking text.
- Appendix allowed but overall length must stay ≤2 pages.
- Outline milestones and assign team responsibilities.

## Team Structure & Submission

- 13‑14 teams total; some topics duplicated across teams.
- Teams assigned or self‑selected; work on given topic.
- One group submission per topic; all members receive same grade.
- Store files in shared group folder (recommended).
- Deadline around the 19th; extra‑day extension approved (no objections).

## Validity & Reliability in Research

- Reliability: consistent results on repeat runs.
- Validity: results reflect true phenomenon.
- Internal validity – correct constructs, unbiased analysis.
- External validity – generalizability beyond sample.
- Address threats in brief paragraphs; acknowledge limitations and fixes.

## Mining Software Repositories – Perils

- Benefit: large open‑source data for empirical SE studies.
- Peril 1: Rewriting history (rebasing/force‑push) hides true timeline.
- Peril 2: Ignoring merges or flattening branches loses integration context.
- Peril 3: Inconsistent timestamps after rewrites.
- Peril 4: Long‑lived branches without frequent merges cause integration difficulty.
- Need careful mapping of branch relationships; avoid assumptions.

## Practical Tips for Repo Analysis

- Treat repo as directed acyclic graph of branches, merges, commits.
- Use git blame and fault‑localization algorithms to trace bug origin.
- Commit every change, even failed attempts, to preserve full history.
- Access individual branch repos when possible to resolve ambiguities.
- Collaborate on formulas via Overleaf or shared link (Discord).
