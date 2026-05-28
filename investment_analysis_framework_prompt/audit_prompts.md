# Audit Prompts

A reference of prompts used across different tools for investment analysis auditing and generation.

---

## Claude Code — General Audit Prompt

```
The file has been revised since.
Conduct a fresh independent audit / review of the file section by section.
Make sure the assumptions made in the document are in alignment with the investment thesis and the numbers used in the document, for instance: a conservative DCF calculation should really reflect growth
assumptions in line with reality and the current business struggles, rather than simply assuming a 5% or 8% growth rate, similarly for all scenarios that are being modelled to form investment conclusions.
Assumptions should be sane enough like how Buffett would approach them, rather than a fairy tale of growth and optimism.
Flag any inconsistencies in any figures or calculations that have been used in the document and that might affect investment conclusions, minor rounding up of figures are fine, as the investment conclusions
would highlight a range rather than zero-in on a single number.
If there are inconsistencies found, jot them down and list them all.
Create a todo list (by breaking the task down in smaller tasks) at the beginning for set of sections and as you go along keep updating the todo file and then finally compile the list of all inconsistencies
found.
Write this entire analysis of issues or inconsistencies that you found in a file, and fan out subagents with claude sonnet to audit different sections of the report independently and the parent agent can
compile the findings and act as an orchestrator.
Ensure you follow the strict compliance guidelines / checklist as per the file: @investment_analysis_framework_prompt/Buffett_Analysis_Compliance_Checklist.md when evaluating / conducting the audit.
File to be analysed is: @<FileName>
```

---

## Claude Code — Subsequent Audits Prompt

```
The analysis file: @<FileName> has been revised since, can you run the same analysis again.
```

---

## Claude Code — Intelligent Chat Compaction Prompt

```
/compact summarise the context from the review findings so far into the chat, and also preserve the inconsistencies and issues that were found in the latest round of review
```

---

## Claude Desktop — Analysis Generation Prompt

```
Analyse <CompanyName>, you can browse this screener link: https://www.screener.in/company/<TICKER>/consolidated/ or any other sources on the web for all the information you need. Make sure to adhere to the file format as per the project level instructions, and create a dedicated todo list for generating the analysis file making sure that you go ahead section by section validating each section as you write it so as to prevent any inaccuracies or mistakes, as the data in each section needs to be accurate and consistent, there should not be any inaccuracies, mathematical or factual or otherwise. Make sure to check items from the todo list once they are completed, keeping it up to date.
```

---

## Claude Desktop — Analysis Revision Prompt

```
First verify if the stated problems exist in the revised markdown file: @<FileName>. Make targeted fixes to the document to ensure consistency and sanity and make sure you address all the issues stated in the review document. Make sure no changes regress back or introduces new issues in the document. Make sure all references in all section were updated correctly and there are no stale references remaining, also make sure that the trends and narratives are consistent and in line with the revised numbers (in case the numbers change). Check if any further changes are truly required or not, if these inconsistencies are due to the raw data gathered from screener, then avoid changing it, you can maybe add a note below it saying the raw data from screener shows this. Make sure the final deliverable is fully compliant with the latest project instructions. Also do a full sweep for any claims that are in contradiction to the document/thesis.
```
