# ECS272 Reading Report 5 - Detailed Explanations with Sources

This document provides in-depth explanations of the answers with direct quotes from the source paper.

---

## Paper Information

**Title:** Mapping Color to Meaning in Colormap Data Visualizations

**Authors:** Karen B. Schloss, Connor C. Gramazio, A. Taylor Silverman, Madeline L. Parker, Audrey S. Wang

**Publication:** IEEE Transactions on Visualization and Computer Graphics, 2018

---

## Summary Sources

### Overview and Research Question

From the Abstract (page 1):
> "To interpret data visualizations, people must determine how visual features map onto concepts. For example, to interpret colormaps, people must determine how dimensions of color (e.g., lightness, hue) map onto quantities of a given measure (e.g., brain activity, correlation magnitude). This process is easier when the encoded mappings in the visualization match people's predictions of how visual features will map onto concepts, their inferred mappings."

> "In this study, we investigated how inferred color-quantity mappings for colormap data visualizations were influenced by the background color. Prior literature presents seemingly conflicting accounts of how the background color affects inferred color-quantity mappings. The present results help resolve those conflicts, demonstrating that sometimes the background has an effect and sometimes it does not, depending on whether the colormap appears to vary in opacity."

### Three Types of Biases

From page 2:
> "There are three types of biases that could determine inferred mappings, which have different implications for the role of the background. A dark-is-more bias [9, 26, 30] implies people infer that darker colors map to larger quantities, regardless of the background color. A contrast-is-more bias [22] implies people infer that higher-contrast colors map to larger quantities, which depends on the background (i.e., dark is more on light backgrounds; light is more on dark backgrounds). An opaque-is-more bias implies people infer that more opaque colors map to larger quantities, which depends on the background in the same manner as the contrast-is-more bias, but only when the colormap appears to vary in opacity."

### Main Findings

From the Abstract (page 1):
> "When there is no apparent variation in opacity, participants infer that darker colors map to larger quantities (dark-is-more bias). As apparent variation in opacity increases, participants become biased toward inferring that more opaque colors map to larger quantities (opaque-is-more bias). These biases work together on light backgrounds and conflict on dark backgrounds. Under such conflicts, the opaque-is-more bias can negate, or even supersede the dark-is-more bias."

From page 2:
> "The role of the background differs depending on the kind of color scale used to construct the colormap and its relation with the background. The background only matters if the colormap appears to vary in opacity."

> "When colormaps do not appear to vary in opacity, inferred mappings are dominated by a dark-is-more bias with no effect of the background. This finding challenges a pure version of the contrast-is-more bias."

> "When colormaps do appear to vary in opacity, inferred mappings contain an opaque-is-more bias. The strength of the opaque-is-more bias depends on the strength of apparent opacity variation."

---

## Question 1: Explain each of the three types of biases the paper discusses and provide an example.

### Dark-is-more Bias

From Section 2.1.3 (page 3):
> "Early empirical work in cartography reported a dark-is-more bias [9]. When presented with choropleth colormaps with no legend, participants inferred that darker regions represented larger quantities."

From page 3:
> "A subsequent eye-tracking study found that participants fixated on the legend less often and were more accurate at answering questions for 'conventional' lightness-based choropleth maps with dark-more encoding, compared with 'unconventional' hue-based colormaps [1]."

### Contrast-is-more Bias

From Section 2.1.3 (page 3):
> "McGranaghan [22] suggested the dark-is-more bias is a special case of a contrast-is-more bias, in which people infer that darker colors map to larger quantities on light backgrounds, but lighter colors map to larger quantities on dark backgrounds."

> "McGranaghan [22] tested this hypothesis by asking participants to interpret choropleth colormaps presented on white, gray, and black backgrounds when there was no legend to specify the encoded mapping. Participants inferred that darker colors represented larger quantities for all three background conditions, but this effect was significantly reduced on the black background."

From page 3:
> "Brewer [5] suggested that although higher values are usually represented by darker colors, this mapping can be reversed on dark backgrounds, as long as there is clear legend specifying the mapping."

### Opaque-is-more Bias

From page 3:
> "If so, people may have an opaque-is-more bias, which to our knowledge, has not yet been empirically tested."

> "A colormap should appear to vary in opacity when the color scale is constructed by linearly interpolating between a reference color and a perceptually distinct background color. In the resulting color scale, the reference color is the highest contrast, or most distinct color from the background. Parts of the image containing the reference color appear as opaque foregrounds, and parts containing intermediate colors appear as foregrounds with varying amount of opacity, overlaid on the background."

From Figure 3 caption and discussion (page 3):
> "Figure 3 (left) illustrates conditions in the natural world that could produce the kind of apparent variation in opacity that is relevant to colormaps. Here, a surface with heterogeneous levels of opacity is superimposed on a homogeneous background. A similar percept might occur if discrete figural elements vary in density on a given background (e.g., variation in density of chocolate powder on whipped cream or density of snow on asphalt)."

### Why Opacity Variation Matters

From page 3:
> "In Roth et al.'s [34] value-by-alpha maps shown in Figure 2A and B, there are two reference colors, saturated red and saturated blue. These colors are interpolated with the background color, which produces intermediate colors that appear to vary in opacity."

> "In contrast, the color scale used in McGranaghan's [22] study (approximated in Figure 2C and D) curved in color space in a manner that would impede apparent variation in opacity on black or white backgrounds. That is, the lightest and darkest colors were low in saturation and the mid-level lightness colors were high in saturation, which would not occur if either endpoint was a reference color that varied in opacity."

---

## Question 2: In the first experiment did the background have different effects depending on the color scale? Explain how the biases were affected, if at all.

### Overall Pattern

From Section 3.2 (page 5):
> "Critical for our question of how inferred mappings depend on the background, there was a 3-way interaction between encoded lightness mapping, background, and color scale (F(3,87) = 13.94, p <.001, η²p = .325). As evident in Figure 5A, participants showed a dark-is-more bias for the Autumn, Hot, and Blue color scales, although it was reduced for the Blue color scale on the black background. The pattern was different for the Gray color scale, with faster RTs for dark-more encoding on the white background but no difference on the black background."

### Autumn and Hot Color Scales

From page 5:
> "For Autumn, Hot, and Blue, there were main effects of encoded lightness mapping, with dark-more encoding resulting in faster RTs (F(1,29) = 28.19, 41.62, 17.85, ps <.001, η²p = .493, .589, .381, respectively). This effect did not interact with the background for Autumn or Hot (Fs <1)..."

### Blue Color Scale

From page 5:
> "...but did interact with the background for Blue (F(1,29) = 7.58, p = .010, η²p = .207). Despite this interaction, RTs for Blue were faster for dark-more encoding on both white backgrounds (F(1,29) = 19.74, p <.001, η²p = .405) and black backgrounds (F(1,29) = 9.72, p = .004, η²p = .251)."

### Gray Color Scale

From page 5:
> "For Gray, RTs were overall faster for dark-more encoding (F(1,29) = 9.82, p = .004,η²p = .253), but that was driven by the difference within the white background condition (F(1,29) = 30.98, p <.001, η²p = .516). Encoded lightness mapping interacted with background (F(1,29) = 21.05, p <.001, η²p = .421), with faster RTs for dark-more encoding on the white background as stated above, but a trend toward faster RTs for light-more encoding on the black background (F(1,29) = 3.31, p = .079, η²p = .102)."

### Opacity Variation Index

From page 5-6:
> "Why did the background have different effects depending on the color scale? A possibility is that the color scales differed in their degree of apparent opacity variation. By viewing the colormaps along the x-axis in Figure 5A, it may be observed that the Gray colormaps appear to vary in opacity, the Blue colormaps somewhat appear to vary in opacity, and the Autumn and Hot colormaps do not appear to vary in opacity."

From page 6:
> "We quantified these deviations in what we call an Opacity Variation Index defined as, log(z+1), where z is the root mean squared error (RMS) between each point in the color scale and the line between the highest-contrast color and the background. We used log RMS because we reasoned that small deviations from the line would strongly affect apparent variation in opacity, but the effect of further increasing the deviation should level off as apparent variation in opacity is broken."

### Relationship Between Opacity Variation and Bias

From page 6 and Figure 6:
> "On the white background, RTs were especially faster for dark-more encoding when there was greater evidence for opacity variation (smaller Opacity Variation Indexes), which can be explained as cooperating dark-is-more and opaque-is-more biases. The opposite was true for the black background, which can be explained as conflicting dark-is-more and opaque-is-more biases."

From page 6:
> "In summary, Experiment 1 demonstrated that when color scales did not appear to vary in opacity, inferred mappings were dominated by a dark-is-more bias, regardless of the background. However, as evidence for opacity variation increased, inferred mappings became increasingly more influenced by an opaque-is-more bias. When the background was white, the opaque-is-more bias reinforced the dark-is-more bias (i.e., faster RTs for dark-more encoding). When the background was black, the opaque-is-more bias contradicted, and thereby dampened the dark-is-more bias."

---

## My Analysis and Opinion

### Why Background Effects Vary Across Color Scales

The key insight from this paper is that not all colormaps are affected equally by background color. The critical factor is whether the colormap appears to vary in opacity, which depends on the trajectory through color space.

**Linear interpolations** (like Gray: black to white) strongly appear to vary in opacity because they're straight lines between an endpoint and the background. These show strong background effects.

**Curved paths** (like Autumn and Hot) don't follow linear interpolations, so they don't appear to vary in opacity. These show minimal background effects and maintain the dark-is-more bias regardless of background.

**Intermediate cases** (like Blue) partially follow linear interpolations and show moderate background effects.

### Practical Implications

1. **For robust colormaps:** If you need colormaps that work on any background (slides that might be printed or presented on different screens), use color scales that curve through color space and avoid linear interpolations. Encode larger values in darker colors.

2. **For value-by-alpha maps:** If you're specifically designing for a known background, linear interpolations (value-by-alpha) can work well, but they won't be robust to background changes.

3. **Design trade-offs:** There's a tension between using apparent opacity as an encoding dimension and maintaining consistent interpretations across backgrounds. You can't have both.

### Methodological Strengths

The response time method is clever because it measures implicit biases rather than explicit judgments. People might consciously try to be consistent if directly asked, but response times reveal automatic interpretations.

The Opacity Variation Index provides a quantitative way to predict which colormaps will be affected by background, which is useful for design tools.

### Open Questions

The paper raises interesting questions about whether these biases come from natural world experiences (ink density, pigment concentration) or learned conventions from maps and visualizations. The fact that they found such strong effects suggests deep-rooted associations, but cross-cultural studies or studies with populations unexposed to data visualization could help distinguish these accounts.

---

## References

Schloss, K. B., Gramazio, C. C., Silverman, A. T., Parker, M. L., & Wang, A. S. (2018). Mapping Color to Meaning in Colormap Data Visualizations. IEEE Transactions on Visualization and Computer Graphics.
