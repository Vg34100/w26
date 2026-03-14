# ECS260-SE | W08-Mon | 2026-02-23

## Action Items

- Let the professor know if you want to pursue publishing a paper
- Review the linked advanced paper; consider using ChatGPT as a helper
- Aim for a score of 4 or higher on the short‑look rubric before submitting
- Prepare concise comments and scores for your team’s work

## Publishing Guidance

- Scoring 1 = don’t bother, 5 = paper‑ready
- Scores 3–4 are borderline; consider submitting if you’re close
- Professor will provide tailored suggestions for each team
- Offer to continue receiving help from the professor on the class

## AI Concepts Overview

- Discriminative vs. generative models: discriminative predicts labels, generative models learn full data distribution
- Intermediate representations compress data into smaller, meaningful forms
- Assumption: data has internal structure that can be captured by compact formulas

## Model Architectures & Techniques

- Transformers use attention to map inputs to outputs, often outperforming CNNs for code/image tasks
- GANs create adversarial setups to generate data that differs from real samples
- Contrastive learning helps models recognize internal structures by comparing examples
- Fine‑tuning and prompt‑tuning adapt large models to specific tasks

## Hardware & Performance

- ASICs (application‑specific integrated circuits) embed model parameters for faster inference
- Token throughput examples: \~120 tokens/s (standard) vs. \~14 k tokens/s (new “Jerry Chat”)
- Hardware limits (GPU memory, compute) still affect model scalability

## Model Alignment & Ethics

- Fine‑tuning a RLHF model can degrade its alignment, leading to unsafe outputs
- Uncensored models may produce more profanity but aren’t necessarily unaligned
- Risks: hallucinations, bias, harmful suggestions (e.g., self‑harm, extremist content)

## Practical Tips & Tools

- Be precise in prompts (e.g., request Unicode, specify math) for better results
- Use structured output formats to simplify downstream processing
- Leverage LLMs for summarization, translation, code debugging, but verify accuracy
- Explore open‑source models for custom fine‑tuning; consider parameter‑fusion techniques
