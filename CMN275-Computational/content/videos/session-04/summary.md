# CMN SESSION 4 - Artifical Intelligence

## AI History & the “AI Winter”

- Early 1950s Dartmouth workshop launched systematic AI research.
- Prominent founders: Marvin Minsky, Claude Shannon, John McCarthy, etc.
- Expectation: solve language, abstraction, and self‑improvement in a summer.
- Results fell short → funding and interest dropped in the 1970s‑80s (AI winter).
- Revival began with the data‑driven machine‑learning approach.

## Types of Machine Learning

- **Supervised learning** – train on labeled examples to predict known categories (e.g., image classification, safety‑gear detection).
- **Reinforcement learning** – agents maximize cumulative reward through trial‑and‑error (e.g., Atari game mastery).
- **Unsupervised learning** – discover hidden patterns without explicit goals (e.g., gender‑bias word associations).
- Each type flips the classic “data → algorithm → goal” pipeline on its head: data + goal → algorithm.

## Bias, Fairness & Mitigation

- Large‑scale text analysis can reveal gender and racial stereotypes (e.g., male names linked to executives, female names to parents).
- Reducing bias often incurs only a tiny drop in accuracy; eliminating bias completely may sharply hurt performance.
- Strategies: remove sensitive variables (gender, race) or apply algorithmic audits to cut bias while preserving most accuracy.

## Training vs. Inference

- **Training**: adjust model parameters using data and an objective function.
- **Inference**: apply the trained model to new, unseen inputs (e.g., a phone app labeling photos).
- Using the test set for training is a “sin” that invalidates performance evaluation.

## Neural Networks & Deep Learning

- Neural nets mimic brain‑like layers: input → hidden layers → output.
- **Convolutional nets** excel at image tasks; **recurrent nets** handle sequences (speech, text).
- **Deep nets** have many hidden layers, enabling complex feature extraction.
- Back‑propagation updates weights by propagating error gradients backward through the network.

## Transformers & Attention Mechanisms

- Transformers process the entire input in parallel, using self‑attention to focus on relevant parts.
- “Attention is all you need” (2017) sparked the rise of large language models (LLMs).
- Positional encoding preserves order while self‑attention captures context across long sequences.
- LLMs predict the next token, giving them human‑like fluency but not guaranteed truthfulness.

## Overfitting, Regularization & Hyperparameters

- Overfitting: model fits training data too closely, failing on new data (e.g., high‑degree polynomial through every point).
- **Regularization** penalizes unnecessary parameters, encouraging simpler models.
- **Hyperparameters** (e.g., number of layers, learning rate) control model capacity; they’re tuned on a validation set, not the test set.
- Proper split: training → validation → independent test ensures unbiased performance estimates.

## Data Explosion & Digital Footprints

- Modern AI thrives on massive, continuously generated data (social media, browsing history, sensor streams).
- Companies collect thousands of personal variables (demographics, interests, device usage).
- Digital footprints feed ML pipelines, but also raise privacy and surveillance concerns.
- Tracking pixels, cookies, and platform SDKs (e.g., Facebook Pixel) monitor user behavior across sites.

## AI Alignment & Ethical Risks

- Aligning ML objectives with human values is critical to avoid harmful outcomes.
- Unsupervised models can inherit societal biases present in training data.
- Reinforcement learning with human feedback (RLHF) helps steer models toward desirable behavior.
- Ongoing research focuses on algorithmic audits, bias mitigation, and ensuring models don’t act contrary to intended goals.

## Practical Applications Highlighted

- Safety‑gear detection in industrial settings saves lives by flagging missing equipment.
- Predicting patient creatinine levels in intensive care illustrates regression use, but also the need to interpret correlations cautiously.
- Real‑time image labeling on mobile devices demonstrates inference at the edge.
- Large‑scale language models (ChatGPT, GPT‑4) showcase the power of transformers for text generation and conversational AI.
