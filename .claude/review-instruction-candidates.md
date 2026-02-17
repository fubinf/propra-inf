# Review Instruction Candidates

Derived from GitHub issues in fubinf/propra-inf.

## From SQL tasks

**Task naming conventions must follow project-wide rules.**
Check whether the task filename and title follow the established naming conventions of the project (e.g., correct prefix casing, use of language-specific identifier conventions). Inconsistent naming breaks regularity across the course. Look for the filename prefix matching the taskgroup convention and the rest reflecting language-specific constructs. Feedback: "The task name does not follow our naming convention. The prefix should be X and the rest should reflect the language's own naming style for consistency across the course."

**Task title should be descriptive enough to convey the topic at a glance.**
Check whether the task name meaningfully communicates what the task covers. Vague names like "advance" or "misc" (when used more than once) make it hard for students and instructors to understand the scope. Subtitles and section headings should also help readers quickly find "what is where." Feedback: "The task name is too vague to be useful. It should hint at the concrete constructs or concepts the task covers."

**Difficulty level must match the actual demands of the task.**
Verify that the declared `difficulty` level is consistent with the amount of guidance, number of new concepts, and complexity of the exercises. A task introducing many new concepts cannot be difficulty 1. A task labeled difficulty 2 must provide step-by-step guidance, documentation pointers, and hints for harder steps. Feedback: "This task introduces too many new concepts / provides too little guidance for its declared difficulty level. Consider adjusting the difficulty or adding more scaffolding."

**Each new concept or term must be introduced before use.**
Check that no technical term, keyword, or concept appears unexplained. Terms must not "fall from the sky." If a concept is used that has not been covered in a previous task (via `assumes` or `requires`), it must be explained in the current task or a documentation pointer must be provided. Feedback: "The term/concept X appears without introduction. Either explain it here, add an `assumes` dependency to a task that covers it, or provide a documentation link."

**Documentation references must be specific and their purpose must be clear.**
When a task says "you can also read the documentation," students do not know whether reading it is required for the task, optional background, or a reference for specific steps. Each documentation link should clarify: Is this mandatory or optional? Which aspect should they look for? For difficulty 2, give precise coordinates (section, page). For difficulty 3, a pointer to how to find the right section suffices. Feedback: "This documentation reference is too vague. Clarify whether students need to read it now, what to look for, and how extensively."

**Exercises should be interleaved with explanatory text, not bunched at the end.**
Check whether the task front-loads too much theory before students get to do anything. Long theoretical sections without hands-on exercises are demotivating and pedagogically suboptimal, especially at lower difficulty levels. Exercises should appear soon after introducing the relevant concept. Feedback: "The task has a long theoretical section before any practical exercise. Move some exercises earlier to break up the theory and let students apply concepts as they learn them."

**A task should stay focused on what its name and goal promise.**
Verify that the task does not silently introduce major concepts that belong in a separate task. If a task titled "JOIN" also teaches GROUP BY, HAVING, and aggregate functions, those unannounced topics should be split into their own task or the task should be renamed. Feedback: "This task covers concepts (X, Y) that go beyond its announced scope. Either rename/restructure the task or extract those parts into a separate task."

**The goal section type must match the actual learning objective.**
Check that the SECTION::goal type (product, idea, experience, trial) accurately reflects the task. If the task is about learning and practicing rather than producing a deliverable, `goal::product` is wrong. Feedback: "The goal type `product` does not match this task. The objective is learning/experiencing, not producing a specific artifact. Use `idea`, `experience`, or a combination."

**Submission section must not contain leftover or incorrect INCLUDE directives.**
Check that the submission section only includes the INCLUDE files that match the actual submission markers ([EQ], [EC], [ER]) used in the task. Leftover includes from earlier drafts (e.g., a Markdown submission include when only snippet markers are used) are confusing and error-prone. Feedback: "The submission section includes X, but this does not match the actual submission types used in the task. Remove the outdated include."

**Ambiguous instructions must be clarified, especially for difficulty 2.**
Look for instructions that can be interpreted in multiple ways. For example, "update a field to today's date" is ambiguous (static date vs. dynamic function). At difficulty 2, every step should be unambiguous without requiring external research or asking an AI. Feedback: "This instruction is ambiguous: it could mean X or Y. At this difficulty level, please make the expected approach explicit."

**Heading levels should be used sparingly and consistently.**
Check that the task does not overuse heading levels (e.g., level-4 headings throughout). Too many headings make the task feel restless and fragmented. For moderate complexity, restrict headings to level 3. Instructions or commands should not be formatted as headings. Feedback: "There are too many sub-headings, making the task visually restless. Consolidate sections and restrict to level-3 headings for moderate-complexity tasks."

**Sample solutions must go into the private altdir, not the public source file.**
Verify that instructor solutions and sample answers are placed in the `altdir` submodule (private repo), not directly in the public task file. The public file should only contain an INCLUDE directive pointing to the private content. Feedback: "The sample solution is in the public source file. Move it to `altdir/` and replace it with an INCLUDE directive."

**Always check the rendered HTML output before submitting for review.**
The rendered output (from `sedrila author`) may reveal formatting problems invisible in raw Markdown: visible triple-backticks, broken list formatting, missing backquotes around code, or stray macro names. Both the student-facing and the INSTRUCTOR section should be visually inspected. Feedback: "There are rendering issues in the generated HTML (e.g., visible backticks, broken lists, missing code formatting). Please run `sedrila author` and inspect the output before submitting."

**Use backquotes consistently for all technical identifiers and code.**
Check that all SQL keywords, function names, table names, column names, file paths, and other technical identifiers are enclosed in backticks. Inconsistent formatting (some in backticks, some in plain text) is confusing and looks sloppy. Feedback: "Technical identifiers like X appear without backquotes. Please consistently use backtick formatting for all code and technical terms."

**References to other tasks should use PARTREF, not vague phrases.**
Avoid phrases like "in the previous task" because students may not work tasks in the expected order. Always use `[PARTREF::taskname]` to create an explicit, clickable reference. This is especially important when a dependency is only `assumes` (not `requires`), meaning students may not have done the other task. Feedback: "Replace the vague reference 'in the previous task' with a concrete `[PARTREF::taskname]` link."

**Line length and formatting should support readable diffs.**
Lines should be at most 100-120 characters. Each sentence should start on a new line. Hyperlinks should go on separate lines. There should be blank lines after headings. These conventions ensure diffs are readable during review. Feedback: "Lines are too long / sentences are not on separate lines, making diffs hard to read. Please follow the formatting conventions in how-to.md."

**Timevalue estimates should be computed from itemized sub-estimates.**
Check that the overall `timevalue` is plausible by mentally (or explicitly) estimating time for each section. Insert time-estimate comments (e.g., `<!-- time estimate: 15 min -->`) after logical sections and sum them up. Authors tend to overestimate time for individual steps. Feedback: "The timevalue seems too high/low. Please break it down into per-section estimates and recompute the total."

**Tasks that grow too large should be split.**
If a single task covers many unrelated or loosely related concepts and becomes very long, consider splitting it into two or more focused tasks. A task named "misc" is acceptable once, but not twice. Each task should have a coherent theme. Feedback: "This task is too large and covers too many loosely related topics. Consider splitting it into focused sub-tasks with clearer scope."

**Data setup instructions must be explicit at low difficulty levels.**
If the task requires students to work with specific data (tables, datasets), it must be clear how they get that data into their environment. At difficulty 2, do not assume students can figure out data loading on their own. Either provide the exact commands or reference a previous task that taught the method. Feedback: "It is unclear how students are supposed to get this data into their environment. At difficulty 2, provide explicit instructions or reference the task where this was taught."

**Taskgroup index pages should be concise.**
The `index.md` for a taskgroup should provide a brief overview and useful cross-cutting documentation links, but should not become an extensive tutorial in itself. Keep it short unless there is a strong reason (e.g., a very broadly relevant topic) to make an exception. Feedback: "The taskgroup index page is more extensive than typical. Keep it concise -- just an overview and key documentation links."

**Open-ended questions need clear expectations in the instructor section.**
When a task includes open-ended reflection questions, the INSTRUCTOR section must specify what constitutes a minimally acceptable answer. Without this, instructors cannot grade consistently. Focus expectations on the key learning insight rather than exhaustive coverage. Feedback: "The instructor section does not clarify what a minimal acceptable answer to this open-ended question should contain. Please specify the essential points students should address."


## From Go tasks

**Insufficient guidance in easy tasks.**
When a task is marked as easy (difficulty 2), students expect step-by-step guidance. Check whether the task introduces syntax or concepts without showing the student how to use them. For example, telling students to "declare a module name" without ever showing the syntax is a gap. Feedback: "This step requires knowledge that has not been taught yet. For an easy task, either provide the syntax explicitly or link to a source where students can find it."
(From #6: prechelt noted students at difficulty "easy" have "a right to be fed with a well-formed spoon" when new syntax is needed.)

**Introducing concepts that are only hinted at, not explained.**
Check whether a task mentions an advanced concept in passing without properly explaining it or deferring it to a later task. Half-introduced concepts create cognitive stress, especially when the task is already dense. Look for phrases like "you will learn more about X later" that leave the concept dangling. Feedback: "Either explain the concept sufficiently for students to work with it, or remove the mention entirely and introduce it in its proper task."
(From #6: prechelt criticized mentioning interfaces without explanation in a basics task where "the head is already quite full.")

**Unexplained notation or jargon in code examples.**
Review code examples and format strings for notation that beginners may never have encountered (e.g., printf-style format specifiers like `%d`). If such notation appears, it must be explained or linked to documentation. Feedback: "This notation is not self-explanatory for beginners. Add a brief explanation or a link to documentation."
(From #6: prechelt noted `Sprintf("%d"` is "pure gobbledygook" for those who have never seen it.)

**Comparisons to other languages without context.**
When a task draws parallels to another programming language (e.g., Python), the comparison must be announced and framed. An unlabeled code snippet in a different language can confuse rather than help. Check that cross-language comparisons are clearly labeled, optionally placed behind a FOLDOUT for those who do not know the other language. Feedback: "This comparison to [language] appears without introduction. Either label it clearly or place it in a FOLDOUT so students unfamiliar with [language] are not confused."
(From #6, #76)

**Implicit behavior that should be made explicit.**
When a task describes behavior that has non-obvious consequences (e.g., type conversion truncation, implicit copying), the concrete result should be stated explicitly, not left for the student to infer. Look for statements about behavior that do not show what actually happens. Feedback: "The result of this operation is not obvious. State the concrete outcome explicitly, possibly with an example."
(From #6: prechelt said "x modulo 256 comes out, right? Then one should write that.")

**Tasks requiring students to produce invalid artifacts.**
Check whether a task instructs students to create something that is not valid in the target language or tool (e.g., a file that is not valid source code). Producing invalid artifacts contradicts the learning goal and risks confusing memory of correct patterns. Feedback: "Asking students to produce an invalid [artifact] undermines learning. Restructure the submission so that students always produce valid [artifacts]."
(From #6)

**Too much passive reading without active tasks.**
Long stretches of explanatory text without interleaved exercises or questions cause students to lose engagement and retention. Check whether there are sections longer than roughly one page of text without an [EQ], [EC], or [ER] marker that requires the student to do something. Feedback: "This section has a long stretch of reading without student activity. Add a question or small exercise to break up the text and activate learning."
(From #6, #9, #82)

**Task is too long and should be split.**
When a single task covers many topics and requires substantial stamina, it should be broken into smaller, focused tasks. Check whether the timevalue exceeds roughly 1.5 hours or whether the task covers more than two or three distinct concepts. Feedback: "This task covers too many topics and is very long. Consider splitting it into smaller tasks, each focused on one concept."
(From #9)

**Advanced material that does not belong in a basics task.**
Check whether a task at introductory level includes material that is too advanced for the target audience (e.g., `unsafe` pointers in a basics task, `defer` stacks in an introductory task). Advanced material should be deferred to a dedicated follow-up task. Feedback: "This material is too advanced for an introductory task. Move it to a separate, higher-difficulty task."
(From #9, #82, #76)

**Ambiguous or underspecified programming exercises.**
Programming assignments must specify behavior for all relevant cases, including edge cases. Check whether the task description leaves open what should happen in certain situations. Feedback: "The programming exercise does not specify what should happen when [edge case]. Please clarify."
(From #9)

**Technically incorrect definitions or explanations.**
Verify that definitions and technical explanations are precise. Common errors include confusing a value with a variable, using "the" with something that has multiple instances, or making claims that do not match the language specification. Feedback: "This definition is technically incorrect: [specific error]. Suggested correction: [correction]."
(From #76)

**Content that is a foreign body in the task's narrative.**
Check whether any section of the task introduces material that is not connected to what comes before or after and is not used by any exercise. Such sections feel pasted in from elsewhere. Feedback: "This section on [topic] is not connected to the rest of the task. Either integrate it by adding exercises that use it, or move it to a task where it fits naturally."
(From #76)

**Code examples with values that coincide with indices.**
When presenting array or list examples, ensure that the element values do not coincide with their indices (e.g., `[0, 1, 2, 3]`), because this creates ambiguity about whether a number refers to a value or an index. Use distinctive values instead. Feedback: "The example values coincide with the indices, making it ambiguous. Use distinct values (e.g., 10, 20, 30) to avoid confusion."
(From #9)

**HINT titles that do not describe the student's symptom.**
The title of a [HINT] block should describe the situation from the student's perspective -- the symptom they are experiencing that would make them want to open the hint. Check that HINT titles are not phrased as topic labels but as descriptions of what the student is stuck on. Feedback: "The HINT title should describe the symptom from the student's perspective (e.g., 'I do not understand what X means') rather than being a topic label."
(From #79)

**"Read this article" without a focused reading assignment.**
Sending students to read an external article without a specific guiding question is poor pedagogy. The task should say "find out X from this article" or "in this article, look for the answer to Y." Feedback: "Replace the generic reading instruction with a focused question that tells students what to look for in the linked resource."
(From #79)

**Exam-style knowledge questions instead of hands-on exploration.**
In a lab course, questions should arise from doing, not from rote recall. Check whether reflection questions can be answered only by reciting facts rather than by experimenting or building something. Feedback: "These questions read like exam questions. In a lab course, prefer questions that arise from hands-on experimentation, where students first try something and then reflect on what happened."
(From #102)

**Purely phenomenological treatment without conceptual grounding.**
Check whether a task only shows how to use a feature without ever explaining the underlying concept or linking to proper documentation. A university-level course must provide conceptual grounding, not just how-to instructions. Feedback: "This task shows how to use [feature] but never explains the underlying concept. Please provide conceptual grounding: a glossary entry, a link to the specification, or a brief explanation."
(From #102)

**Theory-first ordering when practice-first would be more engaging.**
When a task covers both theory and practice, check whether the ordering is appropriate. For a lab course, it is often better to let students experiment first and then explain what happened. Feedback: "Consider restructuring so students do the practical part first and then read the theory, which helps them understand what they experienced."
(From #102)

**External sources that contain misleading or incorrect claims.**
When a task links to blog posts or articles, verify that the linked source does not contain dubious claims that could teach students incorrect mental models. Feedback: "The linked source contains a questionable claim: [specific claim]. Either replace the source, or reframe the task to have students critically evaluate the claim."
(From #85)

**Missing practical relevance or motivation for a concept.**
When introducing a concept, the task should make clear why the student should care. Check whether the task explains the practical benefit or shows a motivating use case. Feedback: "The task shows how [concept] works but does not explain why it is useful. Add a motivating example or use case."
(From #102)

**Submission type mismatch with the actual exercise.**
Check that [EQ], [EC], and [ER] markers match what the student is actually asked to do. An [ER] marker on a question that asks "what do you notice?" is wrong because the answer is a reflection, not code. Feedback: "The marker [EX] does not match the exercise type. Use [correct marker] instead."
(From #85, #23)


## From Web tasks

**Technical claims must be factually correct.**
When the task makes claims about how a technology works, check whether those claims are accurate. Oversimplification is acceptable, but misleading statements that would cause students to form wrong mental models are not. Feedback: "This claim is factually incorrect: [specific error]. Please correct it to avoid teaching wrong mental models."
(From #30: `var` and `let` described as synonymous; #40: question asked the reverse of the correct relationship.)

**Prerequisite knowledge must not be silently assumed.**
Every concept, API, or technique that students need must either have been introduced in a prior task (via `assumes`/`requires`) or be introduced within the task itself with a reading reference. Feedback: "This step uses [concept] which has not been introduced in any prerequisite task. Please add an explanation or an `assumes` entry."
(From #30, #40, #81)

**Research questions at easy difficulty need concrete reading pointers.**
When a task asks students to "research" something at difficulty 2, it must provide a specific URL or documentation reference as a starting point. Feedback: "This research instruction lacks a concrete source. At difficulty 2, provide a specific reading pointer."
(From #30, #46)

**Sample solutions must be instructor-oriented, not just dumps of code.**
The INSTRUCTOR section should highlight which specific aspects matter, what the minimum acceptable solution looks like, and what common mistakes to watch for. Large code blocks without commentary force instructors to mentally diff the entire solution. Feedback: "The sample solution needs markers or annotations pointing instructors to the key aspects they should check."
(From #27, #30, #40)

**Link text must be descriptive, not generic.**
Hyperlinks should have meaningful link text that helps readers scan the document. Generic text like "here" or "this page" provides no information when skimming. Feedback: "Use descriptive link text (e.g., 'JavaScript data structures on MDN') instead of 'hier'."
(From #30)

**Task scope must stay focused -- move tangential topics to separate tasks.**
When a task includes sections on advanced or tangential topics that go beyond the stated learning goal, these should be moved to dedicated follow-up tasks. Feedback: "This section goes beyond the task's learning goal. Move it to a separate follow-up task."
(From #44, #52)

**Examples must match the students' known reference frame.**
When introducing concepts by analogy to a known language, the examples must be semantically equivalent. Use the simplest available form rather than advanced shorthand that has no counterpart in the reference language. Feedback: "This example has no equivalent in [reference language] and will confuse rather than clarify. Use a simpler form."
(From #30)

**Content that logically belongs in a different task must be relocated.**
When a task introduces foundational concepts that are prerequisites for multiple other tasks, those concepts should be taught in the appropriate foundational task, not hastily covered as a side note. Feedback: "This concept belongs in a foundational task (e.g., an HTML task), not here. Relocate it and add an `assumes` dependency."
(From #30, #44)

**Task names must accurately reflect the content.**
The task filename and title should describe what the task actually covers. If a task named "DOM-Klassen" does not involve the DOM at all, the name is misleading. Feedback: "The task name does not match the content. Please rename."
(From #81)

**Redundant or near-duplicate questions should be consolidated.**
When multiple questions test essentially the same knowledge, they waste student time without additional learning benefit. Feedback: "Questions FX and FY are redundant. Merge or replace one with a question covering a different aspect."
(From #44)

**Questions that appear in prose must be marked with [EQ] or removed.**
If the task text poses a question to the student, it must either be marked with [EQ] so it counts as a submission requirement, or be restructured as a rhetorical passage. Feedback: "This question posed in the text is not marked with [EQ]. Either add the marker or rephrase as a statement."
(From #53)

**Template HTML or starter code should be in a separate INCLUDE file.**
When a task provides a template or starter file, this should be extracted into a separate file and included via INCLUDE rather than inlined in the Markdown. Feedback: "Extract this template code into a separate include file for easier maintenance."
(From #27, #34)

**Conceptual explanations must be precise, not hand-wavy.**
When a task explains how something works internally, the explanation must be accurate at the level of detail it chooses to present. Vague phrases that give a false sense of understanding are worse than no explanation. Feedback: "This conceptual explanation is too vague to be useful. Either make it precise or remove it."
(From #81, #52)

**Content volume must be appropriate to the difficulty level.**
For easy tasks, the scope should be limited to the most important items. Presenting exhaustive lists overwhelms students and dilutes the learning focus. Feedback: "This list is too extensive for an easy task. Trim to the essentials."
(From #46, #30)

**Jargon used in questions must be explained first.**
When questions use technical jargon, those terms must have been introduced earlier in the task or be accompanied by an explanation. Feedback: "The term [X] is used without explanation. Please define it before using it in a question."
(From #46)


## From Werkzeuge tasks

**Redundancy with assumed or required tasks.**
Check whether the task re-explains or re-does something already covered by a task listed in `assumes` or `requires`. Feedback: "This is already covered in [prerequisite task]; remove the redundant treatment or change the dependency."

**[EC] markers must match actual executable steps.**
Check that every `[EC]` marker is placed on a step where the student genuinely executes a command whose result matters for learning. Feedback: "This [EC] does not correspond to a meaningful command; remove it or restructure the step."

**Submission section and sample solution must stay consistent with instructions.**
When task instructions change, the command protocol, sample solution, and submission section must be updated in lockstep. Feedback: "The command protocol / sample solution does not match the current instructions; please redo it."

**Author must have personally executed the finished task.**
Check whether commands, outputs, and file paths are internally consistent. Inconsistencies indicate the author did not walk through the task end-to-end. Feedback: "The commands and outputs are inconsistent, suggesting the task was not self-tested. Please execute it yourself and fix discrepancies."

**Exercises for options must make the option's effect visible.**
When teaching a command-line option, the exercise data must be chosen so that using the option produces visibly different results from not using it. Feedback: "The example data does not make the effect of option X visible; add data or restructure so the option demonstrably changes the output."

**Exercises need realistic, motivating scenarios.**
Each exercise step should explain why someone would use the feature in practice, with a concrete, believable scenario. Feedback: "This step lacks a realistic scenario showing why one would use this feature."

**Sub-section headings must be informative, not generic.**
Headings like "Useful Options" or "Advanced Techniques" do not help students re-find specific information. Each heading should name the concepts/commands covered. Feedback: "This heading is too generic; rename it to include the specific concepts, e.g., 'Recursive search with `-r`'."

**Dependencies on knowledge not yet available.**
Check every command or concept used against the `assumes`/`requires` chains. If the task casually uses something not introduced by any prerequisite, students may get stuck. Feedback: "This step uses [concept/command] which is not covered by any prerequisite task; add an `assumes` or explain locally."

**Avoid an overly casual or chatty tone.**
Check whether the writing style is factual or uses humor, slang, or rhetorical flourishes. Casual language creates ambiguity. Feedback: "The tone here is too informal; please rewrite in a factual, concise style."

**Ambiguous action directives.**
Check whether each instruction makes unmistakably clear what the student should do. Phrases like "let's look at..." leave unclear whether the student should execute, read, or think. Feedback: "It is unclear whether the student should actually do something or just read; please use an explicit directive."

**Conceptual tasks need a clear learning roadmap.**
For tasks that aim to build a mental model, check whether there is an explicit outline of concepts to be learned, visible at the outset. Each concept should be accompanied by at least one active step and ideally an [EQ]. Feedback: "This task aims to teach a mental model but lacks an upfront list of concepts and structured progression."

**Platform-diversity pitfalls.**
Check whether instructions work across all platforms students might use (Windows/WSL, native Linux, macOS). Feedback: "This task assumes [specific platform feature]; consider whether it works on all student platforms."

**Factually incorrect claims about tool behavior.**
Watch for statements about how a tool works that are simply wrong. Such errors teach incorrect mental models. Feedback: "The claim 'X' is factually incorrect; [correct explanation]. Please fix."


## From Bibliotheken tasks

**Reading references must be specific, not vague.**
When sending students to documentation, name a specific page, section, or function -- not just "read the documentation." For difficulty "easy," each sub-task should have its own targeted reading pointer. Feedback: "The reading reference for step X is too broad. Please point to the specific section or API page."

**Do not give away the answer right before asking the question.**
If a task provides a code snippet or explanation and then immediately asks a question whose answer is already stated, the question becomes trivially pointless. Feedback: "The solution to FX is essentially already stated in the preceding paragraph. Either remove the preceding explanation or make the question more challenging."

**Questions should produce genuine learning, not busywork.**
Every question [EQ] should teach something relevant. If a question merely asks for a trivial fact that does not deepen understanding, it wastes time. Feedback: "This question does not clearly advance the learning objectives. Consider replacing it with a more substantive question."

**Use correct technical terminology for programming constructs.**
Authors frequently confuse "method" vs. "function," "expression" vs. "command," "property" vs. "method." Such imprecision damages students' mental models. Feedback: "plt.plot() is a free function, not a method. Please use the correct term."

**Avoid unnecessary verbosity around code identifiers.**
Writing "the function `model_dump_json()`" is wordy when simply "`model_dump_json()`" suffices. Feedback: "Drop the category label; the identifier speaks for itself."

**Instructor section must exist and must be useful for tutors.**
Every task needs an [INSTRUCTOR] section that repeats question/task labels with brief expected answers and indicates review priorities. Feedback: "The [INSTRUCTOR] section is missing / does not repeat the question labels / does not indicate review priorities."

**Terminology must be consistent within a task and across a task group.**
If a task group introduces specific terms in the first task, later tasks must not switch vocabulary without explanation. Feedback: "The terminology fluctuates: earlier tasks say X but here you write Y. Please use the term introduced in the first task."

**Documentation links should point to stable versions, not dev.**
When linking to library documentation, use the stable/release URL rather than the development version. Feedback: "Please link to the stable documentation, not the dev version."

**Tasks at difficulty "easy" must provide feedback on correctness.**
If an easy task asks students to write code but provides no way to verify their results (no expected output, no assertions), students may silently produce wrong answers. Feedback: "Students get no feedback on whether their result is correct. Add expected output, row count, or similar verification."

**Task scope must match the course's learning goals -- do not teach domain science.**
If a task on library X starts teaching the underlying domain (statistics, physics, math) rather than how to use the library, it has drifted out of scope. Feedback: "This part teaches domain knowledge rather than the library itself. Either remove it or replace it with a link to external background."

**When a task assumes knowledge from prerequisite tasks, do not re-explain it.**
Background sections should not repeat what was already covered in assumed or required tasks. Feedback: "This explanation is redundant with what is covered in [PARTREF::X]. A brief reference suffices."

**Concise writing is essential -- students are reluctant readers.**
Every sentence must earn its place. Look for filler phrases, unnecessarily long background sections, and bullet lists where comma-separated lists would suffice. Feedback: "This section is too verbose. Please cut to the essentials."

**Tasks should help students build correct mental models, not just execute steps.**
Especially for libraries with confusing semantics, the task should explicitly identify conceptual pitfalls and guide students toward a clean mental model. Feedback: "This is a known conceptual pitfall. The task should explicitly warn about it and help students build the right mental model."

**Reading instructions should precede the first task that requires the knowledge.**
If a task asks students to do something without first sending them to read how it is done, students at difficulty "easy" will feel lost. Feedback: "The student is asked to do X but has not been sent to read about it first. Add a targeted reading reference before this step."

**Distinguish `assumes` from `requires` correctly.**
`requires` means the student builds on artifacts produced in the prerequisite; `assumes` means the student needs the knowledge but not the artifacts. Feedback: "Task X is listed as `requires` but its products are not used here. Change to `assumes`."

**Marker types ([EC], [EQ], [ER]) must match the actual task type.**
[EC] marks commands for a command protocol, [EQ] marks questions for a markdown document, [ER] marks code requirements. Using the wrong marker confuses students and the submission system. Feedback: "Step X uses [EC] but the student is writing code, not executing a command. Use [ER] instead."

**For easy tasks, prescribe variable names to simplify checking.**
When students are asked to store results in variables, giving a specific variable name makes the instructor's job of checking much simpler. Feedback: "At difficulty 'easy,' please prescribe a variable name to make checking easier."


## From C/Python/RegExp/Testen tasks

**Insufficient HINT blocks for harder steps.**
When a task at difficulty 2 or 3 contains steps that are not immediately obvious, it should provide [HINT] blocks. Check each instruction step: could a weaker student get stuck? Feedback: "Step X could be difficult for some students. Please add a [HINT] with the needed approach."
(From #4, #72)

**Task not tested by the author before submission.**
Commands that do not work, links that are broken, or code examples with errors indicate the author did not work through the task end-to-end. Feedback: "Please work through the entire task yourself before submitting. The command/link/code at step X does not work as described."
(From #16, #72)

**Redundant content that duplicates assumed/required tasks.**
A task should not re-explain material from prerequisite tasks. Conversely, check that all needed prerequisites are listed. Feedback: "This explanation is redundant with task X which is already in 'assumes'. Remove it or add an 'assumes' entry if missing."
(From #10, #61)

**Redundant text across platform variants.**
When a task provides instructions for multiple platforms, check for duplicated text blocks. Identical blocks should be consolidated using INCLUDE snippets. Feedback: "The Windows and Linux instructions are nearly identical. Please extract shared parts into an INCLUDE snippet."
(From #10)

**Background section contains non-motivational content.**
The [SECTION::background] is meant only for motivation. Technical details or cross-references do not belong there. Feedback: "The background section contains technical details that belong in the instructions section. Background should only motivate the topic."
(From #24, #26)

**Example too simple to motivate the concept being taught.**
When teaching a testing method or analysis technique, the example must be complex enough that the technique is visibly useful. Feedback: "The example is too simple to show why this technique is needed. Please use a more realistic or complex example."
(From #24, #42, #146)

**Steps unrelated to the learning goal distract from it.**
At difficulty "easy," preparatory steps should be given as direct commands without extended explanation. Feedback: "The explanation of X is not the learning goal and distracts at difficulty 'easy'. Give it as a direct instruction without elaboration."
(From #16)

**Asking open questions without ensuring prerequisite knowledge.**
Reflection questions only work if sufficient background knowledge has been established. Check whether each question can be meaningfully answered given what the student knows at that point. Feedback: "Question X asks students to reason about Y, but they have no basis for this yet. Provide the needed background first."
(From #68, #24)

**Scenario or narrative is unrealistic.**
When a task uses a scenario to motivate exercises, the scenario must be plausible. Effects that cannot actually happen as described make the narrative confusing rather than engaging. Feedback: "The scenario described here is unrealistic. Either make it plausible or drop the narrative framing."
(From #16, #67)

**Instructor hints are incomplete or out of date.**
After task revisions, the INSTRUCTOR section may no longer match the current content. Check that numbering matches and sample solutions are complete. Feedback: "The instructor section references step numbers that no longer exist. Please update it."
(From #16, #68)

**Germanization of English terms handled poorly.**
When English technical terms are used in German text, inflected English forms like "matched" are incorrect; use the German equivalent or adapt to German grammar. Feedback: "Please do not use English inflected forms in German text. Use the German term or adapt consistently."
(From #72)

**Missing glossary entries for key terms.**
When a task introduces domain-specific terminology, corresponding glossary entries should exist with TERMREF links. Feedback: "The task uses several domain terms without glossary entries. Please create entries and add TERMREF links."
(From #14)

**Conceptually difficult topics introduced too abruptly.**
Some concepts are inherently surprising or complex. Check whether the task provides enough gradual buildup. The introduction should explain why the concept exists before showing how to use it. Feedback: "The concept of X is introduced too abruptly. Add an explanation of the problem it solves before showing the mechanism."
(From #4, #67)

**Task offers unnecessary choices that complicate grading.**
When a task says "do A or B" and the downstream steps differ, this creates complexity for both students and tutors. If one fixed path simplifies the rest, remove the choice. Feedback: "The choice between A and B complicates subsequent steps and grading. Please pick one approach."
(From #16)

