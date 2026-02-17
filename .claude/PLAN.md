# Work out reviewing heuristics

Development director prechelt needs to perform a review of each task that reaches state `alpha`
before it can go to `beta` and be deployed.
These reviews are very difficult, because the kinds of problems pertinent for a taskgroup
are different per taskgroup topic and per author.
Also, prechelt often does not have strong expertise in those topic areas.

Nevertheless, dozens of review procedures have already taken place, often over multiple rounds.

Our goal here is working out rules and heuristics that Claude can use to perform the discovery
of problem candidates automatically so that prechelt's task becomes easier.

Review discussion is in GitHub issues. 
A task located in file ch/mychapter/mytaskgroup/mytask.md may or may not have a corresponding issue.
If it has, the subject of that issue will be mychapter/mytaskgroup/mytask (typos and renames permitting).
Be aware that parts of the issue may refer to earlier versions of the task that are no longer visible
in the workdir. 

Use the following procedure:
- Work through all issues and corresponding tasks, presumably using a fresh subagent per taskgroup.
- From each task/issue pair, derive one or more candidates for reviewing instructions.
  That is, abstract from the specific problem discussed in the issue to a problem type
  that might occur in multiple tasks of this taskgroup or other taskgroups:
  What is the problem type? How to look for it? How to phrase feedback?
  Keep it concise; add just enough detail that you can make sense of it again later.
- Append each such candidate instruction to file .claude/review-instruction-candidates.md
  as one paragraph. Some redundancy is OK, especially inter-taskgroup, but avoid massive redundancy.
- When you are through with all issues, consolidate the list into a shorter one with somewhat
  larger categories (perhaps with subcategories), illustrated by examples from potentially several
  topic areas. 
  Discriminate content-related problems (regarding the task as such) from 
  form-oriented ones (spelling, sentence construction, formatting, etc.).
- Put this list into .claude/review-instructions.md. This is the work result.
