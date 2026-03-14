# STA220-DATA | W09-Tue| 2026-03-03

## Action Items

- Upload the two required HTML files (deadline today)
- Submit your presentation PDF by 1 PM on your presentation day
- Prepare a 12‑15 min talk + 5 min discussion (max 20 min)
- Review the first two homework assignments before the next class
- Read the full announcement sheet and note the office‑hour schedule
- Run a quick Python demo of tf‑idf → cosine similarity on sample sentences
- Experiment with a Naive Bayes gender classifier (name‑letter features) and plot an ROC curve

## Announcements & Deadlines

- Two HTML assignments due today; upload to the course portal
- Presentation PDFs due 1 PM on the day you present
- Total lecture time next week: 100 min across five sessions (1 h 40 min)
- No discussion section on the listed days (Monday, Tuesday, Thursday)
- Project submission deadline: next Sunday; expect extra office‑hour help

## Presentation Guidelines

- Slides: 12‑15 min presentation, followed by 5 min discussion
- Keep total time ≤ 20 min; first group may get 10 min only
- Upload PDFs early so the professor can download before class
- Actively participate in Q&A; ask at least one question during discussion

## Office Hours & Support

- First day: office hours 9 AM – 12 PM (skip 12:45‑1:45 PM)
- Monday: 1 PM – 3 PM for project‑related queries
- Thursday: regular weekly slot (time as usual)
- Other questions: email the professor or post on the course forum

## NLP Lecture Overview

- **Pipeline:** tokenization → preprocessing → bag‑of‑words → tf‑idf → similarity / classification
- **Zipf’s law:** rank vs. frequency follows a log‑log linear trend
- **Sparse matrices:** store term counts efficiently; many zeros for large vocabularies
- **Binary encoding:** presence/absence reduces impact of very frequent words

## Similarity & Classification Techniques

- **Cosine similarity:** angle between tf‑idf vectors; 1 = identical, 0 = orthogonal
- Example with four sentences: two nearly identical, one distinct, one unrelated
- **Naive Bayes gender classifier:** use letter‑frequency features of names
  - Compute empirical probabilities, then posterior via Bayes rule
  - Choose a decision threshold (commonly 0.5) to label male/female
- **Threshold tuning:** affects false‑positive/true‑positive rates; visualize with ROC curve

## Evaluation Metrics

- **ROC curve:** plot true‑positive rate vs. false‑positive rate across thresholds
- **AUC (area under curve):** larger area → better overall classifier performance
- Adjust threshold to balance sensitivity vs. specificity for the task

## Topic Modeling (LDA)

- Steps: tokenize → remove stopwords → tf‑idf → fit LDA model → extract topics
- Applied to chapter‑level documents; discovered two main topics (e.g., story vs. biology)
- Model accuracy ≈ 87 % on test set; 29 chapters mis‑classified
- Highlights limitation of bag‑of‑words: order information lost, mitigated by n‑grams

## Practical Tips

- Use Python libraries: scikit‑learn for tf‑idf & cosine, nltk for tokenization, gensim for LDA
- For Naive Bayes, sklearn.naive_bayes.MultinomialNB works with character n‑gram features
- Visualize ROC with sklearn.metrics.roc_curve and auc functions
- Remember to normalize vectors before computing cosine similarity

---

*Prepared for Pablo’s NLP class.*
