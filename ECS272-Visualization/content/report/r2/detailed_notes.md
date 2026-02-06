# ECS272 Reading Report 2 - Detailed Notes

## Paper: The Science of Visual Data Communication: What Works
**Authors:** Franconeri, S. L., Padilla, L. M., Shah, P., Zacks, J. M., & Hullman, J.
**Published:** Psychological Science in the Public Interest, 2021

---

## Summary - Extended Version with Sources

### Power of Visualization

**Direct Quote (p. 113):**
> "Visualizations allow powerful processing of an entire two-dimensional rectangle of information at once, in stark contrast to the limitation of reading handfuls of symbolic numbers per second."

**Visual Channels (p. 113-114):**
The paper identifies several visual channels that transform numbers into images:
- **Position**: Used in dot plots and scatterplots
- **Length/Area**: Used in bar graphs (both position of tips and one-dimensional lengths)
- **Area**: Circles used to overlay values on maps
- **Angle**: Emerges when points are connected in line graphs
- **Intensity**: Luminance contrast or color saturation in heat maps

**Quote on Statistics Limitations (p. 113):**
> "Because statistics summarize larger sets of numbers by abstracting over them and making assumptions about the patterns that they might contain, many sets of numbers can generate the same statistics."

This is demonstrated through Anscombe's Quartet (Figure 1), where four datasets with identical means, standard deviations, and correlation coefficients look completely different when visualized.

### Visual Channel Precision Ranking

**Quote (p. 114):**
> "This list is ordered by the typical precision with which a viewer can verbally state the ratios between the two values shown; more precise ways of communicating numbers are at the top and less precise ways are at the bottom."

The ranking from most to least precise:
1. Position (highest precision)
2. Length
3. Area
4. Angle
5. Intensity (lowest precision)

**Why Position is Preferred (p. 114):**
> "Because position is the clear winner for precision, visualization designers often prioritize the vertical and horizontal dimensions of two-dimensional space when depicting or organizing quantitative data."

### Visual System Capabilities

**Fast Global Statistics (implied throughout):**
The visual system can quickly compute statistics across entire images - means, trends, correlations.

**Slow Individual Comparisons (p. 116):**
The paper discusses how "making comparisons among subsets of values is slow and limited to two or three comparisons per second."

---

## Question 1: Perceptual Illusions - Detailed Breakdown

### Illusion 1: Non-Zero Baseline

**Location in paper:** Pages 116-117, Figure 2 and Figure 3

**Direct Quote (p. 116):**
> "For example, see the dot plot and bar graph at the top of the second column of Figure 2. The dot plot uses position as its visual channel, and the bar graph depicts the same data with both position and length. The second value appears to be roughly double the first value. Look more closely at the y-axis: The second value is only about 1% bigger than the first; the difference appears greater because the axis baseline does not start at zero."

**Real-World Example - Fox News Chart (p. 116-117):**
> "In March 2014, a version of the bar graph at the upper right appeared on Fox News... Around 6 million U.S. citizens had signed up for a new health-care program sponsored by the president, and the government specified a goal of 7 million sign-ups by March 31. Although the numbers presented are honest (a 6:7 ratio), the visualization's truncation of the y-axis tells a different story (a 1:3 ratio) to the viewer's visual system."

**Empirical Evidence (p. 117):**
> "Using a visualization similar to the Fox News example, researchers asked crowdsourced workers to rate the contrast between the two depicted values on a 1-to-5 scale. Ratings in a zero-baseline condition averaged around 1.5, whereas ratings in a deceptive-baseline condition averaged 2.8."

**Key Finding - Persistence of Effect:**
> "Moreover, the deceptive effect persisted when participants were asked to type the numeric values represented by each bar before making their effect-size rating and were reminded of the y-axis's truncation."

This shows that even when people are explicitly aware of the manipulation, the visual illusion still affects their judgment.

**References cited:**
- Pandey et al., 2014, 2015
- Correll et al., 2020
- Hofman et al., 2020

### Illusion 2: Area vs. Length Confusion

**Location in paper:** Page 118, Figure 4

**Direct Quote (p. 118):**
> "In a classic example at the top left of Figure 4, values are encoded by one-dimensional length (the height of each person), producing a 1:2 ratio of the two numbers. However, you might find that your estimate of the depicted values is determined instead by the area taken up by each person, leading to something closer to a 1:4 ratio (or even a 1:16 ratio, if the icons suggest three-dimensional volume)."

**Evidence of the Error:**
> "People do indeed make this error, even when the numeric data are printed saliently near the visual representation (Pandey et al., 2015)."

**Broader Application - Bubble Charts:**
Applies to any visualization using circles where viewers must determine if radius or area encodes the value. The confusion can "change the extracted value by an order of magnitude."

---

## Question 2: Common Visual Distortions - Detailed Breakdown

### 1. Non-Zero Baseline Distortion
*(See Question 1 detailed notes above)*

### 2. Line Graph Distance Illusion

**Location:** Page 118, Figure 4 (center)

**Direct Quote (p. 118):**
> "In the line graph in the middle of Figure 4, the two curves are identical (y = x³), but the darker line is translated vertically upward by a constant of 1,000. Even if the viewer knows that the two shapes are identical, it is difficult to see that the vertical distance between the two lines is the same across their entire horizontal span."

**Why this happens:**
> "Instead, given any point on the dark line, viewers tend to see its distance from the closest point on the gray line, which becomes progressively smaller as both lines increase. This illusion makes it difficult to visually estimate differences between lines, especially lines with steep slopes."

**Solution Mentioned:**
> "This illusion is well known to electrophysiology researchers: When faced with visualizing the difference between two measured waves, they will explicitly plot a 'difference wave' that shows the difference as a single line."

**Reference:** Cleveland & McGill, 1984

### 3. Intensity/Color Contrast Effects

**Location:** Page 118, Figure 2 (bottom)

**Direct Quote (p. 118):**
> "Both on the map and in the rectangle, the two vertically separated circles have the same luminance value. However, the lower circle is subjectively darker to the eye because it has been placed on a lighter background and has a higher contrast with its surroundings."

**Why this happens biologically:**
> "In the real world, converting luminance to contrast is a critically important mechanism for seeing accurate luminance and color despite changes in the brightness and color profile of light in the environment (Purves et al., 2004). However, this correction leads to misperceptions of intensity-coded values in the artificial world of data visualizations."

**Design Rule:**
> "One rule of thumb is never to plot intensities on top of other intensities that vary, as in the map in Figure 2."

**Reference:** Szafir, 2018

### 4. Categorical Perception in Color

**Location:** Pages 118-119, Figure 4 (bottom left)

**Direct Quote (p. 119):**
> "A classic example is the seven discrete colors that we see in a rainbow, which are not present in the rainbow itself. Those color categories are created by an automatic process that systematically bins continuous wavelengths into one of several perceptual categories, exaggerating metric differences among values that straddle those boundaries."

**Application to Visualization:**
> "This same phenomenon occurs when data are depicted by hues... These additional hues create new color-category boundaries that can dramatically exaggerate the differences between values that straddle them."

**Example Given - The Economist Cover:**
Referenced in Figure 3: "the blue-to-red scale creates a salient categorical color boundary at the color transition point, which makes the temperature increase in the past few years especially salient."

**Also Affects Other Channels:**
> "Similar category boundaries can affect the perception of values depicted by other channels such as position or length. In a pie graph or stacked bar graph, values that are near gridlines or the implicit 50% mark in the middle of the bar or pie are recalled as being farther from that category boundary."

**References:**
- Y. Liu & Heer, 2018
- Quinan et al., 2019
- Ceja et al., 2021
- McColeman et al., 2021

### 5. Three-Dimensional Projection Distortions

**Location:** Page 118, Figure 4 (top right - donut chart)

**Direct Quote (p. 118):**
> "If the viewer can recover the actual three-dimensional geometry from the two-dimensional depiction, then the values should be accurately perceived. By contrast, if the viewer pulls values from the two-dimensional image (the amount of green or purple pixels on the screen), the values in the 'front' will be inflated because of the perspective projection. Unfortunately, this technique is indeed substantially misleading because static two-dimensional projections do not typically lead to effective recovery of three-dimensional structures."

**References:**
- Tittle et al., 2001
- Brath, 2014 (counterpoint)

### 6. Integral Representations Problem

**Location:** Page 118

**Direct Quote (p. 118):**
> "Other examples of integral representations include encoding two sets of data in rectangles—one set in their widths and one set in their heights. Instead of seeing these values separately, the eye is tempted to translate them into the aspect ratio and the area of each rectangle. The eye then focuses on the ratios and multiplication of each pair of values."

**Color Example:**
> "As an extreme case, it is unwise to attempt to use the red component of a single color... to depict one number and the green component for another. Red and green will combine in an integral fashion when both are at their highest value, and the viewer will see a single integral percept of yellow."

**Trade-offs with Scatterplots (Figure 4, right):**
> "Once two sets of numbers are combined into a single two-dimensional plot, new integral percepts emerge, such as the distance between any two points across both their x and y values, points that are outliers on both axes, or the global shape of all points that we can easily interpret as a correlation. However, there is a trade-off. The distribution of values of either set in isolation is now tougher to disentangle."

**Solution:** Use "marginal histograms" alongside scatterplots.

**References:**
- Garner, 1974
- Shechter & Hochstein, 1992

---

## Question 3: Techniques for Differentiation - Detailed Breakdown

### Primary Technique: Color

**Location:** Pages 120-122

**Why Color is Superior (p. 121):**
> "Plotting the groups as categorically different colors is often the first choice because the visual system processes color differences more efficiently than shape differences across the two-dimensional visual plane, as measured by performance in visual-search and texture-segmentation tasks."

**Empirical Evidence:**
> "These findings, based on simple displays used in laboratory studies, extrapolated to a data-visualization context in which viewers compared the average heights of multiple color-coded or shape-coded clouds of points in a scatterplot: Color coding produced far better performance (Correll et al., 2012)."

**Reference:** Wolfe & Horowitz, 2017

#### Color Selection Guidelines

**Perceptual Spacing (p. 121):**
> "When color differences distinguish data from two separate groups or classes, differentiating those classes is easier if the encoded colors are farther apart in a perceptual color space. For example, it is easier to differentiate red from blue than from orange-red."

**Tools Mentioned:**
- **ColorBrewer 2.0** (Brewer, 1994a, 1994b): "Researchers have constructed effective palettes from perceptually informed color spaces (e.g., CIELAB)"
- **Colorgorical** (Gramazio et al., 2016): "balances perceptual differentiation with aesthetic considerations"

**Semantic Congruence (p. 121):**
> "Picking a color for a nominal value should also be constrained by the semantic congruence of the value and the color. If the nominal values are lemons and cherries, it is easier for viewers to answer questions about a chart that labels those values with yellow and red, compared with a standard palette that does not consider semantic congruence."

**Automatic Color Selection:**
> "An algorithm can automatically generate intuitive color choices for a given noun by analyzing the color profile of images pulled from Web searches for the noun and then optimizing color assignments in terms of perceptual spacing and semantic fit. Such algorithms can perform as well as human experts in quickly picking color palettes for nominal data."

**References:**
- Lin et al., 2013
- Setlur & Stone, 2015
- Schloss et al., 2018

### Secondary Technique: Shape

**Location:** Page 122

**When to Use Shape:**
> "Sometimes a visualization designer needs to show a second set of nominal values in the same plot... Typically, shape would be used to show that second nominal variable. Because it is less perceptually effective than color, it should be used for the less important variable, or the one with fewer values to differentiate."

**Problem with Default Shape Sets:**
> "The shape sets used in commercial software (e.g., Microsoft Excel) gravitate toward intuitive shapes, such as circles, triangles, squares, and diamonds, that are not actually well separated in perceptual space."

**Perceptual Shape Space Research:**
> "Human shape space (at least for the simple shapes used in visualizations, and at least for the types of tasks tested so far) appears to prioritize the difference between open (circle, square, triangle) and closed (×, +, *) shapes, such that differentiating points is easier when they differ in that property."

**Three-Dimensional Shape Space:**
> "An initial full three-dimensional perceptual shape space (Huang, 2020) adds the additional properties of intersection and spikiness; Figure 6 depicts a clear improvement in shape differentiability compared with the typical sets used even in professional data-visualization software."

**References:**
- Demiralp et al., 2014
- Burlinson et al., 2017
- Huang, 2020

### Double Encoding: Color + Shape

**Location:** Page 122

**Effectiveness (or lack thereof):**
> "Some software automatically differentiates nominal variables with both color and shape, under the assumption that more differentiation is better. However, work has shown that color is already so dominant in its effectiveness that redundant encoding does not substantially improve visual processing efficiency (Gleicher et al., 2013) unless the viewer has color-vision impairments or the viewer's task is exceptionally difficult (Nothelfer et al., 2017)."

**When NOT to Use:**
> "Given anecdotal claims from some expert designers that redundant encoding can cause confusion in viewers, who typically expect color and shape to signal different nominal variables (Tufte, 1983), the lack of evidence for a perceptual advantage suggests that redundant encoding should be avoided in most cases, except when used to make visualizations accessible for viewers with color-vision impairments."

### Accessibility: Color-Vision Impairments

**Location:** Page 120, Figure 5

**Statistics:**
> "Color-vision impairments are estimated to affect 4% of the global population (Olson & Brewer, 1997), or roughly 300 million people. Further, older adults can have less sensitivity to color (Silva et al., 2011)."

**Types:**
> "Some color blindness results in viewers not being able to distinguish between various colors; protanopia, or red–green color blindness, is the most common, but various other versions of color blindness exist."

**Design Solutions (p. 120):**
> "The simplest way to make visualizations accessible to viewers with color blindness is to avoid using hue as the only encoding channel or allow viewers to change the color palette. Designers can also double-encode a variable, using hue and another encoding channel (Plaisant, 2005), as in the second row of Figure 5. The most thorough and inclusive option is to use color palettes that are safe for people with color-blindness, such as those proposed by Harrower and Brewer (2003)."

**Tool:** ColorBrewer 2.0 includes color-blind-safe palettes

---

## Additional Context: Beyond Simple Ratio Judgments

**Location:** Pages 120-122

The paper challenges the simple ranking of visual channels:

**Quote (p. 121):**
> "The ranking derived from performance on two-value ratio judgments does not always extrapolate across these alternative tasks. For example, depicting data with a line graph, which relies on 'precise' position coding, can lead to lower efficiency in seeing big-picture statistical properties such as means. Intriguingly, the opposite is true for intensity coding. Multiple studies have shown that for identifying particular values, position is far more precise than intensity, but for judging an average across many values, intensity is more precise."

This suggests that the "best" visual channel depends on the task viewers need to complete.

---

## Complete Reference List from Extracted Text

All references mentioned in the detailed notes above are cited in the original paper:
- Anscombe (1973) - Anscombe's Quartet
- Cleveland & McGill (1984, 1985) - Visual channel precision ranking
- Heer & Bostock (2010) - Channel precision validation
- Pandey et al. (2014, 2015) - Deceptive baseline studies
- Correll et al. (2012, 2020) - Color coding efficiency, baseline effects
- Y. Liu & Heer (2018) - Color perception
- Wolfe & Horowitz (2017) - Visual search efficiency
- Lin et al. (2013) - Semantic color congruence
- Brewer (1994a, 1994b) - ColorBrewer
- Huang (2020) - Perceptual shape space
- And many more in the full paper...
