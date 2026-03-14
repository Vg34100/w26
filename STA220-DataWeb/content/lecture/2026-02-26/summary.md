# STA220-DATA | W08-Thu | 2026-02-26

## Overview

- Lecture covered preprocessing steps for text analysis
- Focus on removing non‑informative words and standardizing tokens
- Discussed how to build a custom stop‑word list for the specific domain

## Stop Words & Tokenization

- Stop words: common words (e.g., “the”, “and”, “is”) that add little meaning
- Goal: filter out these words before feature extraction
- Tokenization: split text into individual words/tokens
- Lower‑casing each token to ensure uniformity
- Example: from 2,000 raw tokens, \~1,000 remain after stop‑word removal

## Stemming & Lemmatization

- Stemming groups words with the same root (e.g., “wave”, “waving”)
- Lemmatization uses dictionaries to map words to base forms (verb, noun, etc.)
- Can download language‑specific dictionaries (e.g., French) for lemmatization
- Adding POS tags (noun, verb, adjective) can improve downstream analysis

## Term Frequency & Zipf’s Law

- Term Frequency (TF) measures how often a word appears in a document
- Zipf’s law: frequency of a word ≈ (max frequency) / rank
- Example: most common word 40k occurrences → 2nd rank ≈ 20k, 3rd ≈ 13k, etc.
- Useful for estimating word distribution in large corpora

## Current Results

- After preprocessing, reduced vocabulary to \~1,000 unique words
- Original set: \~2,000 words, 915 were stop words
- New set: \~1,071 words, 698 after further cleaning
- Ready to extract features (e.g., TF, TF‑IDF) from the cleaned list

## Next Steps

- Apply the cleaned word list to the full textbook chapters
- Compute term‑frequency vectors for each chapter
- Explore TF‑IDF weighting to highlight distinctive terms
- Review Zipf’s law predictions against actual word counts in the next lecture.
