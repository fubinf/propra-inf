# Task Review Instructions

Consolidated reviewing heuristics derived from ~70 review discussions in GitHub issues.
Organized by category: content-related problems first, then form-oriented ones.
For a task in file `ch/mychapter/mytaskgroup/mytask.md`, 
the corresponding issue will have subject `mychapter/mytaskgroup/mytask`.

---

## A. Content-Related Problems

### A1. Difficulty Level and Guidance

**A1.1 Difficulty level must match actual demands.**
Verify that the declared `difficulty` is consistent with the amount of guidance, number of new concepts, and complexity.
Difficulty 2 ("easy") means step-by-step guidance with documentation pointers and [HINT] blocks for harder steps. If the
task requires significant independent problem-solving, it cannot be difficulty 2.

**A1.2 Easy tasks must provide step-by-step guidance.**
At difficulty 2, students expect to be "fed with a well-formed spoon." Every new syntax element, API call, or concept
must be shown or linked. Do not assume students can figure out non-trivial things on their own. If a step could cause a
weaker student to get stuck, add a [HINT].

**A1.3 HINT blocks for non-obvious steps.**
Check each instruction step: could a weaker student get stuck? If so, is there a [HINT]? HINT titles should describe the
student's symptom (e.g., "I don't understand what X means"), not be topic labels.

**A1.4 Content volume must match difficulty level.**
For easy tasks, limit scope to the most important and commonly used items. Exhaustive lists overwhelm students and
dilute focus.

### A2. Conceptual Clarity and Correctness

**A2.1 Technical claims must be factually correct.**
Verify that definitions, explanations, and technical claims are precise and accurate. Common errors: confusing value
with variable, method with function, expression with command; making claims that contradict the language specification;
inverting relationships between APIs. When a claim sounds surprising, look it up.

**A2.2 Each new concept must be introduced before use.**
No technical term, keyword, or concept may appear unexplained. If it is not covered by a prerequisite task (`assumes`/
`requires`), it must be explained here or a documentation link must be provided. Check the entire assumes/requires
chain.

**A2.3 Half-introduced concepts create cognitive stress.**
Do not mention an advanced concept in passing ("you will learn more about X later") without properly explaining it.
Either explain it sufficiently or remove the mention entirely.

**A2.4 Unexplained notation in code examples.**
Review code examples for notation beginners may not know (e.g., printf-style format specifiers, regex syntax, advanced
shorthand). Such notation must be explained or linked to documentation.

**A2.5 Correct technical terminology.**
Check for imprecise language: "method" vs. "function," "expression" vs. "command" (Befehl vs. Ausdruck), "property"
vs. "method." Imprecision damages mental models.

**A2.6 Definitions and explanations must be precise, not hand-wavy.**
Vague explanations that give a false sense of understanding are worse than none. If a concept is explained, the
explanation must survive careful scrutiny at the chosen level of detail.

**A2.7 External sources must not contain misleading claims.**
When linking to blog posts or articles, verify the source does not contain dubious claims. If problematic, either
replace the source or reframe as a critical-reading exercise.

### A3. Task Structure and Pedagogy

**A3.1 Practice before theory (in a lab course).**
When a task covers both theory and practice, consider whether practice-first ordering would be more engaging. Students
experiment first, then understand. Long theory blocks before any hands-on work are demotivating.

**A3.2 Exercises interleaved with explanatory text.**
Avoid long stretches of text (> ~1 page) without an [EQ], [EC], or [ER] marker. Exercises should appear soon after
introducing the relevant concept.

**A3.3 Questions must produce genuine learning.**
Every [EQ] should advance the learning objectives and require real thought. Questions that ask for trivial facts, or
whose answers are given in the immediately preceding text, are busywork.

**A3.4 Exam-style questions are not ProPra-appropriate.**
In a lab course, questions should arise from doing, not from rote recall. Prefer questions where students first try
something and then reflect on what happened.

**A3.5 Tasks must show practical relevance.**
When introducing a concept, explain why the student should care. Show a motivating use case or practical benefit, not
just mechanics.

**A3.6 Exercises must make the taught feature's effect visible.**
When teaching a command-line option, API feature, or technique, the exercise data must be chosen so that using the
feature produces visibly different results from not using it. Trivial examples where the feature has no observable
effect are useless.

**A3.7 Motivating scenarios must be realistic.**
When a task uses a scenario to frame exercises, it must be plausible. Unrealistic or far-fetched scenarios confuse
rather than engage.

**A3.8 Examples must be complex enough to motivate the concept.**
For testing methods, design patterns, or analysis techniques, the example must be rich enough to demonstrate the
concept's value. Trivially correct examples undermine the "why."

**A3.9 Cross-language comparisons must be framed.**
When drawing parallels to another language, clearly announce the comparison. Unlabeled code in a different language
confuses. Consider placing comparisons in a FOLDOUT.

**A3.10 Code examples: avoid values that coincide with indices.**
In array/list examples, use distinctive values (10, 20, 30) not (0, 1, 2, 3), to avoid ambiguity between values and
indices.

### A4. Task Scope and Dependencies

**A4.1 Task must stay focused on its announced scope.**
A task should not silently introduce major concepts that belong in a separate task. If scope creep occurs, either split
or rename.

**A4.2 Tasks that grow too large should be split.**
If timevalue exceeds ~1.5h, or the task covers more than 2-3 distinct concepts, consider splitting. Each task should
have a coherent theme.

**A4.3 Advanced material does not belong in basics tasks.**
Material too advanced for the target level should be deferred to a dedicated follow-up task.

**A4.4 Content belonging to another task must be relocated.**
Foundational concepts that are prerequisites for multiple tasks should be taught in the appropriate foundational task,
not hastily covered as a side note.

**A4.5 Distinguish `assumes` from `requires` correctly.**
`requires` = student builds on artifacts from the prerequisite. `assumes` = student needs the knowledge but not the
artifacts. Check that the classification matches actual usage.

**A4.6 Do not re-explain content from prerequisite tasks.**
If material is covered by a task in `assumes`/`requires`, do not repeat it. A brief reference suffices.

**A4.7 Do not teach domain science in a programming course.**
Tasks about libraries should teach how to use the library, not the underlying domain (statistics, physics, math). Link
to external resources for domain background.

### A5. Documentation and Reading References

**A5.1 Documentation references must be specific.**
"Read the documentation" is insufficient. Each reference must name a specific page, section, or function. For difficulty
2, give precise coordinates. For difficulty 3, a pointer to how to find the right section suffices.

**A5.2 "Read this article" needs a focused question.**
Do not send students to read an article without a guiding question. Say "find out X from this article" rather than
just "read this."

**A5.3 Reading instructions should precede the first task that requires the knowledge.**
Students at difficulty 2 need to be told what to read before being asked to do something with that knowledge.

**A5.4 Documentation links should point to stable versions.**
Use stable/release URLs, not dev/nightly versions that may change.

**A5.5 References to other tasks must use [PARTREF::...].**
Use the macro, not hardcoded URLs or vague phrases like "in the previous task." Students may not work tasks in the
expected order.

### A6. Exercises and Submissions

**A6.1 Marker types ([EC], [EQ], [ER]) must match the exercise.**
[EC] = commands for command protocol, [EQ] = questions for markdown, [ER] = code requirements for source code.
Mismatched markers confuse students and the submission system.

**A6.2 Submission section must match the actual markers used.**
Only include INCLUDE files that correspond to markers actually used in the task.

**A6.3 Programming exercises must specify edge case behavior.**
All relevant cases must be specified, including edge cases. Ambiguity leads to confusion.

**A6.4 Questions in prose must be marked with [EQ] or removed.**
If the text poses a question, it must have an [EQ] marker or be restructured as a rhetorical passage.

**A6.5 Do not produce invalid artifacts.**
Students should not be asked to create files that are invalid in the target language/tool. This contradicts learning
goals.

**A6.6 Easy tasks: prescribe variable names to simplify checking.**
At difficulty 2, giving specific variable names makes instructor checking much easier.

**A6.7 Easy tasks: provide feedback on correctness.**
If students write code but have no way to verify results (no expected output, no assertion), they may silently produce
wrong answers.

**A6.8 Unnecessary choices complicate grading.**
When "do A or B" creates divergent paths, pick one approach for all students unless the choice itself is pedagogically
valuable.

### A7. Instructor Section

**A7.1 Instructor section must exist and be useful.**
Every task needs an [INSTRUCTOR] section with question/task labels (F1, A1, etc.), brief expected answers, and review
priorities. Tell tutors what to focus on.

**A7.2 Open-ended questions need clear expectations.**
Specify what constitutes a minimally acceptable answer. Focus on the key learning insight.

**A7.3 Sample solutions must be instructor-oriented.**
Do not just dump code. Highlight key aspects, minimum acceptable solutions, and common mistakes. Use
markers/annotations.

**A7.4 Instructor section must stay current after revisions.**
After editing instructions, update the instructor section: numbering, sample solutions, review guidance.

**A7.5 Sample solutions belong in altdir, not the public file.**
Instructor solutions go in the `altdir` submodule. The public file should only have an INCLUDE directive.

---

## B. Form-Oriented Problems

### B1. Text Quality and Style

**B1.1 Concise writing.**
Every sentence must earn its place. Students are reluctant readers. Cut filler phrases, unnecessarily long background
sections, and wordy constructions.

**B1.2 Avoid overly casual or chatty tone.**
Use factual, concise language. Humor, slang, or rhetorical flourishes create ambiguity, especially for non-native
speakers.

**B1.3 Consistent terminology within and across tasks.**
Use the same term for the same concept throughout a task and across the task group. Do not switch vocabulary without
explanation.

**B1.4 Avoid unnecessary verbosity around code identifiers.**
Write "`describe()`" not "die Methode `describe()`." The backtick-formatting already signals the construct type.

**B1.5 Germanization of English terms.**
Do not use English inflected forms ("matched") in German text. Use the German equivalent or adapt to German grammar.

**B1.6 Descriptive link text, not generic.**
Use "JavaScript data structures on MDN" instead of "hier." Descriptive text helps scanning and accessibility.

### B2. Formatting and Structure

**B2.1 One sentence per line, max 100-120 characters.**
Each sentence starts on a new line. Hyperlinks go on separate lines. Blank lines after headings. These conventions
ensure readable diffs.

**B2.2 Heading levels: sparing and consistent.**
Restrict to level 3 for moderate complexity. Too many sub-headings make the task visually restless. Headings should be
informative, not generic ("Useful Options" -> "Recursive search with `-r`").

**B2.3 Use backquotes consistently for all technical identifiers.**
All keywords, function names, file paths, and technical identifiers must be in backticks. No exceptions. Do not inflect
identifiers inside backticks (e.g., avoid "des `DataFrame`s").

**B2.4 Check rendered HTML output before submitting.**
Run `sedrila author` and inspect both student-facing and instructor output. Catch broken formatting, visible backticks,
broken links, stray macro names.

**B2.5 Template/starter code in separate INCLUDE files.**
Extract templates into separate files and use INCLUDE rather than inlining them in the Markdown.

### B3. Naming and Metadata

**B3.1 Task names must follow project conventions.**
Filename prefix must match the taskgroup convention. The rest should reflect language-specific constructs.

**B3.2 Task names must be descriptive.**
The name should clearly convey the topic. Vague names like "misc" (if used more than once) are unhelpful.

**B3.3 Goal section type must match the learning objective.**
Check that `SECTION::goal` type (product, idea, experience, trial) accurately reflects the task.

**B3.4 Timevalue needs per-section estimates.**
For tasks > 1h, add `<!-- time estimate: X min -->` comments after each section and verify the total.

**B3.5 Taskgroup index pages should be concise.**
Brief overview plus key documentation links. Not an extensive tutorial.

### B4. Author Quality Assurance

**B4.1 Author must self-test the finished task.**
Walk through the entire task end-to-end. Commands, outputs, links, and file paths must be internally consistent.

**B4.2 Glossary entries for key terms.**
Domain-specific terminology needs glossary entries with TERMREF links.

**B4.3 Platform diversity.**
Check that instructions work on all supported platforms (Windows/WSL, Linux, macOS). Declare limitations if not.

**B4.4 INCLUDE file references must resolve.**
Verify that all INCLUDE directives point to existing files, including altdir files.

---

*Consolidated from review discussions on SQL, Go, Web, Werkzeuge, Bibliotheken, C, Python, RegExp, and Testen tasks.*
