# Introduction to Advanced Software Engineering Research (Course 260)

The instructor, Vladimir Sokov, opened the first session of course 260, an advanced, research-based software engineering class centered on empirical methods and applied research. He laid out administrative structures, workload expectations, and the multi-stage team project with firm deadlines. The lecture then introduced Empirical Software Engineering (ESE), highlighting what can be observed and validated in software practice, and concluded with a survey of research reasoning modes and philosophical stances that guide study design.

## Course Administration and Expectations

Course 260 is an advanced software engineering class geared toward applied research and producing a publishable project report. It has run for a number of years with documented success: a few papers have been published and more submitted. The course aims to deliver a piece of work that ideally can be submitted immediately to a conference or similar venue; submission is encouraged but not mandatory.

The format is team-based, with about four to five students per team. With 80 enrolled students, the class can handle up to 20–25 teams, and the instructor noted that this team structure has worked well historically. The course emphasizes identifying the bleeding edge in the literature and implementing it to solve practical problems. Lectures blend theory and practice, and the entire course adopts an empirical science perspective to evaluate artifacts, methods, and assumptions.

Workload highlights:
- Weekly reading is expected (chapters and slides). Slides are designed assuming students read or at least skim them before class.
- Weekly quizzes occur at the beginning of the week and remain available through holidays. Additionally, approximately every three lectures, there will be a brief (five-minute) quiz focused on reading tips to encourage preparation.
- A group presentation will help students collect and synthesize research relevant to their chosen project.
- The central project is delivered in three parts, roughly one month apart, aiming for solid preliminary results or an extended abstract ready for publication or submission.
- All project deliverables are graded. There is no final exam; the only assessments are quizzes, the presentation, and the three project components.

Communication guidance:
- Students should post questions on course forums when possible.
- Email is reserved for emergencies.

## Key Personnel and Class Composition

Instructor: Vladimir Sokov introduced himself as having been at the institution for about 10 and a half years, working across data science, AI, and ML with a focus on software engineering. He earned his PhD in 2002.

TA: Ryan Jahangir, a second-year PhD student under Professor Gautam Nitin Kaur, focuses on AI for health. His current research explores improving breast cancer treatment, prevention, and screening using large language models. He previously took this course and performed well.

Office hours will be held by both the instructor and the TA.

Class composition was polled to understand student distribution and interests. The instructor inquired about:
- Non-CS students
- PhD students (approximately “Seven?” were indicated during the poll)
- Master’s students
- Interests across software engineering, programming languages, networking, systems/builders, AI, and other areas such as crypto, graphics, visualization, and quantum computing

Team formation guidance emphasized leveraging diverse strengths:
- Researchers who enjoy deep literature reviews
- Implementers who can find and adapt existing solutions
- Strong writers who craft clear, compelling prose
- Dedicated coders who deliver product increments
- Effective project managers who organize time and resources

The instructor encouraged frank discussion among teammates regarding strengths, noting that aligning tasks with individual strengths improves team performance. Individual work preferences are acceptable within teams as long as collaboration norms are respected; a desire to unilaterally control a project is not conducive to teamwork.

## Project Structure and Key Deadlines

The project is team-based (four to five people per team), with the course able to support up to 20–25 teams and a preferred total of 15–20. With roughly 80 students enrolled, team formation begins immediately.

Deliverables and timeline:
- Team names solidified by January 11.
- Project proposals due on January 16.
- Progress reports due one month after project proposals.
- Final report due on March 18.

Administrative infrastructure and support:
- Once teams are finalized, a team ID, collaboration page, discussion page, and file sharing will be set up via Canvas.
- Piazza will be used for coordination, including a sign-up sheet for different projects.
- It is acceptable for multiple teams to pursue the same project idea.
- Project ideas will be circulated later today or tomorrow morning; students may also propose their own ideas as long as they are at least tangentially relevant to software engineering.
- A resource page will be shared, covering computational and data resources.

Checkpoints and guidance:
- Students should begin discussing projects early and assemble teams promptly.
- Regular checkpoints with instructors are planned.
- There will be a couple of check-in sessions in early March, and individual check-ins with every team to ensure progress in the final two weeks.
- Office hours are often the most productive venue for refining ideas, research questions, motivations, theories, and results.

Assessment summary:
- No final exam or other exams beyond quizzes.
- The project has three graded parts plus the group presentation.

## Foundations of Empirical Software Engineering (ESE)

ESE centers on empirical observation and validation in software engineering, prioritizing applied inquiry over heavy theory. The first two lectures will cover ESE’s primary theoretical aspects while maintaining a practical orientation.

Definitions and scope:
- ESE observes software engineering artifacts—such as code, bug reports, developer discussions, and logs—and validates theories, tools, methodologies, and assumptions through empirical evaluation.
- The field examines what makes software systems, projects, and teams work better, using structured, non–ad hoc methods.

Artifacts and observations:
- Examples include code changes (e.g., number of lines of code incremented or modified), operational logs, and communication records.
- Observation may compare real-life behaviors to simulations or established ground truth.

Complexity and need for structure:
- Large software systems involve extensive codebases, disconnected teams, and hybrid cloud/in-house infrastructure. In mission-critical contexts, even a single-line change can require multiple approvals across a management chain, underscoring the need for rigorous, structured analysis.

Key sub-fields:
- Software evolution: tracking changes across the project life cycle (creation, fixing, maintenance, sunset) and comparing versions.
- Software maintenance: addressing usability-driven issues throughout the system’s lifespan.
- Mining software repositories: analyzing millions of projects (e.g., on GitHub) to understand how processes, development, and maintenance practices evolve over time.

Representative research questions:
- Tool validation: assessing the effectiveness of static code quality tools in detecting defects.
- Methodology comparison: empirical evaluation of agile versus traditional programming approaches using clearly defined metrics.
- Language assumptions: testing claims such as whether strongly typed languages reduce defects.
- Teaming models: comparing “pair programming” versus “single programming” for speed and quality; intuition suggests advantages from combined knowledge, but research indicates pair programming may not increase productivity, though it can improve learning.
- AI-assisted coding: investigating whether rapid initial development leads to higher maintenance burdens later; evaluating which LLM-based coding tools are best requires metrics beyond speed or lines of code because precise expectations and bug detection often emerge only after-the-fact. LLMs often lack best practices and self-checking mechanisms.

Publishing and scientific practice:
- The course will cover AI for SE and SE for AI later in the term, as well as key venues for publishing in this area.
- Research findings should be carefully documented (“memorialized”) and open to review by others.

## Philosophical Approaches to Scientific Inquiry

Modes of reasoning:
- Deductive reasoning: begin with theory, formulate a hypothesis, observe, and test whether observations confirm or refute the theory.
- Inductive reasoning: start from observations, identify patterns, form hypotheses, and build theory—often used when theory is absent or weak.
- Abductive reasoning: select the best explanation that fits the data by enumerating possible explanations and choosing the most plausible; common in machine learning practice.

Study design frameworks:
- Quantitative studies use statistical methods to count and decide with measurable precision.
- Qualitative studies use interviews and surveys to develop richer, context-sensitive explanations.
- Mixed-methods may combine the two depending on the research question.

Human subjects and compliance:
- Any research involving human subjects (including questionnaires) requires IRB approval, which takes a couple of weeks.

Integrated design perspective:
- Place the research question centrally and situate it within philosophical assumptions, strategies of inquiry, and methods.

Philosophical stances:
- Positivism/post-positivism: objective knowledge; causal relationships determine outcomes; reductionist approaches; preferences for quantitative methods; aims to verify or falsify theories.
- Constructivism/interpretivism: socially constructed knowledge; context-relative truth; interpretive flexibility of theoretical terms; preferences for qualitative methods and local theories.
- Critical theory: research as a political act intended to enact change; participatory approaches; choose research based on who benefits and on desired changes.
- Pragmatism/eclecticism: problem-centered; uses multiple methods from multiple perspectives; acknowledges bias in all inquiry; seeks practical outcomes.

Pedagogical emphasis:
- Many in quantitative fields have been trained as positivists or primitives.
- The instructor noted the importance of solving problems without overburdening inquiry with definitional debates, and observed that pragmatists are often waiting to define themselves.

## Action Items

- @Vladimir Sokov
  - [ ] Post project ideas for students to review - [TBD]
  - [ ] Send out an email about static checking positions - [TBD]

- @All Students
  - [ ] Read the assigned chapter before the next class - [TBD]
  - [ ] Start talking about teams and begin assembling members - [TBD]
