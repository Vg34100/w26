# ECS272 Reading Report 4 - Detailed Explanations with Sources

This document provides in-depth explanations of the answers with direct quotes from the source paper.

---

## Paper Information

**Title:** Doom or Deliciousness: Challenges and Opportunities for Visualization in the Age of Generative Models

**Authors:** V. Schetinger, S. Di Bartolomeo, M. El-Assady, A. McNutt, M. Miller, J. P. A. Passos, J. L. Adams

**Publication:** Computer Graphics Forum, Vol. 42, No. 3, 2023

---

## Summary Sources

### Overview and Motivation

From the Abstract:
> "Generative text-to-image models (as exemplified by DALL-E, Midjourney, and Stable Diffusion) have recently made enormous technological leaps, demonstrating impressive results in photographic composition. However, the quality of these results has led to existential crises in some fields of art, leading to questions about the role of human agency in the production of meaning in a graphical medium."

> "Seeking to circumvent similar ponderous dilemmas, we attempt to understand the roles that generative models might play across visualization. We do so by constructing a framework that characterizes what these technologies offer at various stages of the visualization workflow, augmented and analyzed through semi-structured interviews with 21 experts from related domains."

### Study Methodology

From Section 3 (page 3):
> "To better understand the challenges and risks that may arise through the integration of generative models into visualization workflows, we conducted a semi-structured interview study with participants to elicit forecasts, opinions, fears, hopes, and concerns arising from experts from various domains."

> "We conducted interviews with 21 participants, which lasted an average of one hour. Interviews were conducted remotely over Zoom. Participants were drawn from a convenience sample assembled based on their work in relevant domains. In particular, we consulted experts with backgrounds in art or art history (N = 5), machine learning (N = 2), and visualization or HCI (N = 14)."

### Four-Stage Pipeline

From Section 4 and Figure 7 (page 4):
The paper uses a modified visualization pipeline with four stages:
1. **Data-fying** - "Capture an aspect of the world into data"
2. **Transforming** - "Modify or wrangle data into a vis-ready format"
3. **Visualizing** - "Create an image (model or chart) from the data"
4. **Interacting** - "The reader uses the chart to modify the display"

---

## Question 1: How would you use GenAI throughout the four stages of the visualization pipeline?

### Data-fying Stage

From page 5, Section 4.1:
> "Data is not a natural resource, and so its entry into a visualization workflow begins by representing what that data is [MKC20]. This process can be time-consuming and difficult, as data modeling is notoriously challenging [HS17]. A generative model might aid this process by helping the user identify what counts as data..."

On creating synthetic data:
> "Consider creating a subset of data (Fig. 7 left). In such a task, the user asks the model to create a working subset of the data, such as by generating an SQL query for a large database. Such automation might reduce the burden of designing a potentially difficult query, and thereby speed up the analysis or design process."

On training data generation:
> "Curating input data can help reduce biases, personalize models, and increase the general quality of results. The complexity latent in this task type could be allayed by a generative model, which might be able to act as an adaptor, such as in Flores et al.'s data linter [FMG*22], which could provide more dynamic or situational suggestions than heuristically-motivated training-data analysis tools."

### Transforming Stage

From page 5, Section 4.2:
> "Once the data is established, it needs to be transformed into a form that might be pliable for visualization. This process can involve wrangling, processing, introducing additional models (such as through regression or other advanced analytics), or countless additional approaches."

On automation:
> "Within each of these stages, there are opportunities for a generative model to exert agency. For instance, prompts like 'remove outliers' or 'find missing data' presupposes particular structures of the data, while these might sometimes be unambiguous (for instance, a monthly calendar missing data from the weekends has a clearly defined gap), in other cases, it might not be clear (for instance, removing outliers might assume a particular model of the data distribution)."

### Visualizing Stage

From page 6, Section 4.3:
> "The most prominent stage in our pipeline is the visualization stage. Here, the modeled data is mapped to a visual encoding which will subsequently be presented to the user... For instance, some participants (P4_vis, P6_vis, P10_art, P12_vis) highlighted the potential for harm in found graphics that do not handle sensitive content carefully..."

On beautification:
> "One such example is the beautification of visualization designs, which while mostly aesthetic, could also be functional. From the selection of proper colors based on semantics [EAKM*22, HYC*22], to more extreme visual deformations, it was considered by participants to be mostly 'subjective' [P15_vis]."

Chart recommendation (page 7):
> "Generative models could be used to suggest types of charts that have fitting qualities to represent given data. Our discussants used such an example of Tableau's chart recommendation system, which may have caused participants to think of this application as very feasible..."

Rapid iterative prototyping (page 7):
> "Rapid iterative prototyping is the process of rapidly changing parameters while designing or developing a prototype. This aids users in quickly iterate over them. Most participants felt that it could be used both for supporting VIS and supporting a design space that they could explore for more specific, pragmatic purposes."

### Interacting Stage

From page 8, Section 4.4:
> "An illustrative application of this potential is the Personalization (Fig. 7 right) of such a user's tastes, tasks, and abilities. For instance, a model might act as an adaptor and automatically transform a general visualization into one that is accessible to users that are tailored to a user's particular needs, such as color blindness or low visualization literacy (Fig. 8c)."

On tracking user behavior:
> "Such personalization also might be dynamic and rely on tracking user behavior and attention [P5_vis]. While such tools could help to obtain new perspectives, there is also risk that such tools could lead to overview of sense of agency over [Hee19] the presented information."

---

## Question 2: Why is unreliability a concern?

### Unreliability as Primary Concern

From page 8, Section 5.1:
> "Unreliable Results. The unreliability of results was one of the aspects of greatest concern. Most worries stemmed from the intractability or unexplainability of the sources and suggestions. The stochastic nature of generative models and lack of semantic grounding makes it hard (or some might argue, impossible [MGSS21]) to guarantee compliance to queries. Although this is more serious for certain applications where precision is critical (also likely to demonstrate that an image is real, which may incur possible copyright or ownership issues..."

Specific unreliability issues mentioned:

**Lack of semantic grounding:**
> "P6_vis claimed that the risk of copyright violation would be high from generating even minor sections of a visualization. While some of these issues may have a technical solution (such as is promised in Amazon's yet-to-be-released Code Whisperer [Ama22]), navigating the ethical elements beyond the legal ones remains a thorny task."

**Parroting training data without understanding (page 5):**
> "Similarly, there were concerns about the model parroting its training dataset (Fig. 6, right). Some of these stemmed from anxieties about using the material in ways not permitted by the licenses of the data (an issue which is heavily examined in the American court system [Vin22]), and the inability to track down the sources used for the generation."

**Model training on its own outputs (page 5):**
> "If an idea is out of scope of the training data, or if a type of person is biased against, that bias will be embedded into the data, possibly without labeling—an error that can cascade down to affecting every subsequent data interaction. Reciprocally, the use of a model to construct data that might be used to manifest the biases of the user such as through confirmation bias."

### Alternative Perspectives on Reliability

From page 9, Section 5.2:
> "Beyond exploring how to better navigate and convey trust, there is ample room for improvement of generative models, such as performance perspective. For instance, the current resolution for generated images is still quite low, as higher resolutions require enormous amounts of GPU memory. Simply by increasing the maximum resolution, we allow for higher quality images to be rendered, which are essential for text and data visualization."

### Trust and Verification Issues

From page 8-9:
> "Despite the value of these interactions, participants were concerned about both interactions and involuntary misleading information generated through the models. They cited the ability of these models to generate believable misinformation (P1_vis, P19_vis, P21_ML) and mentioned deep fakes (P2_ML and P8_ML and P10_art). P17_vis warned that this could also be involuntary, mentioning the possibility of 'Deepfakes of black art', or just users of these models to be misled by their own results."

On the challenge of verification:
> "P14_vis reiterated the dangers of trusting tools without fully understanding, saying that 'everything that is robust is obvious and everything that is obvious is robust', referencing Da's [Da19] argument that computational literacy can—a mere counting exercise that only manually interact with the text—a failure mode to consider in future systems design."

---

## My Analysis and Opinion

### Why Unreliability is Critical for Visualization

Visualization is fundamentally about truthful communication of data. Unlike generative art where creative interpretation is valued, data visualization serves to inform decisions and reveal insights. When a generative model produces visualizations that look professional but contain inaccuracies, it creates several problems:

1. **Authority without accuracy:** The polished appearance of AI-generated visualizations can lend them undeserved credibility
2. **Difficulty in verification:** Users may not have the expertise to spot subtle errors in chart types, scales, or data representations
3. **Cascading errors:** If these visualizations inform decisions, errors propagate into real-world consequences

### Where GenAI Makes Sense

Based on the paper's findings, GenAI seems most appropriate for:
- **Aesthetic decisions** where there's no single "correct" answer (color palettes, layout spacing)
- **Exploration and ideation** where humans review and validate outputs
- **Augmentation** of human designers rather than replacement

### Where to Be Cautious

The paper suggests caution in:
- **Automated chart selection** without human verification
- **Data transformation** where errors could be subtle and hard to detect
- **Any application where precision matters** more than aesthetics

### The Human-in-the-Loop Imperative

The experts interviewed consistently emphasized keeping humans involved. This aligns with the broader theme in visualization research that automation should augment, not replace, human judgment. The paper's title "Doom or Deliciousness" captures this tension perfectly - these tools offer genuine benefits but also real risks that require careful navigation.

---

## References

Schetinger, V., Di Bartolomeo, S., El-Assady, M., McNutt, A., Miller, M., Passos, J. P. A., & Adams, J. L. (2023). Doom or Deliciousness: Challenges and Opportunities for Visualization in the Age of Generative Models. Computer Graphics Forum, 42(3).
