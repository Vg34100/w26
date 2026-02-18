# ECS251-OS | W05-Mon | 2026-02-09

## Implicit Neural Representations (INR) for Volume Data

- Compact storage: NR weights &lt;&lt; raw volume size
- Typical compression: 1 %–10 % of original volume
- Example: 1 GB → &lt; 100 MB (sometimes \~10 MB)
- Random‑access to continuous values at any coordinate
- No need for grid‑based interpolation in rendering

## Training an INR Model

- Starts from random‑initialized weights (noise volume)
- Query model for sample values, compute loss vs. ground truth
- Optimize weights via gradient descent
- 1 k × 1 k × 1 k volume can train in minutes on a server (with optimizations)

## Shadow Effects in Volume Rendering

- Gradient‑based shading vs. shadow‑enhanced rendering
- Shadows improve surface distinction (e.g., nail vs. body)
- Real‑time shadowing requires secondary ray to light source → high cost
- Pre‑computing shadows doubles memory usage (shadow volume ≈ original volume)

## INR‑Based Shadow Coefficient Volumes

- Represent each pre‑computed shadow volume with its own INR
- Memory‑efficient: compact INR replaces large shadow volume
- Challenge: shadows depend on light direction, transfer function, etc.
- Need a model that generalizes across infinite lighting conditions

## Diffusion Model for Shadow INR Generation

- Leverage diffusion models (from vision) to synthesize shadow coefficients
- First contribution: diffusion framework learns distribution of shadow volumes under varied lighting
- Second contribution: real‑time system generates shadows on‑the‑fly from the trained diffusion model
- No extra runtime computation after diffusion model is pretrained

## Prior Work: Volumetric Ambient Occlusion (VAO)

- Deep‑learning predicts pre‑computed illumination volumes (AO)
- Input: raw volume; Output: AO volume
- Explored transfer‑function conditioning (encoder vs. explicit vector)
- Limitations: expensive 3D CNN training, high memory, limited generalization

## Evaluation Strategy

- Quantitative: image quality metrics (e.g., PSNR, perceptual scores), training time, memory footprint, rendering performance
- Qualitative: visual comparison of generated shadows vs. ground truth, side‑by‑side with VAO baseline

## AI Over‑Reliance in Knowledge‑Graph + LLM Systems

- Users tend to trust AI outputs without verification
- Over‑reliance leads to acceptance of incorrect entity mappings or hallucinated facts
- Need verification support to reduce blind trust

## Pilot Study Design (Knowledge‑Graph Interface)

- Baseline UI: chat panel + two tables (entity mapping, relationship triples)
- Tasks: answer nutrition questions; seeded errors introduced deliberately
- Participants: CS and food‑science students (2 groups)

## Findings on User Verification Behavior

- Users often skip entity‑mapping table → miss mapping errors
- CS students spend more time checking multi‑hop relationships; food‑science students trust KG if context feels right
- Longer textual answers increase likelihood of checking tables first
- Misinterpretation of table ordering (frequency ≠ relevance) observed

## Interface Improvements & Next Steps

- Replace tables with richer visualizations (sub‑query graph, LM thought process)
- Show hierarchical entity matches, confidence scores, citations
- Iterate UI based on pilot feedback; aim for transparent verification without high cognitive load
- Continue refining diffusion‑based shadow generation and integrate with improved volume rendering pipeline.
