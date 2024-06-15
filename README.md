
# ChatRnD
**Current Version: 0.0.1**

A Multi-Agent Framework for Scientific Research and Development (RnD), inspired by the [ChatDev](https://github.com/OpenBMB/ChatDev/) and [CAMEL](https://github.com/camel-ai/camel) frameworks, an extension of the [PhDBot](https://github.com/DreamBrookLabs/PhDBot).

## Project Timeline
**Version 1: Q3 2024 - Q4 2024**

This project aims to develop a proof-of-concept for an upcoming grant proposal to-be-submitted to ResearchHub for Communicative Agents in the University Research Use Case. This project is inspired by the call-for-action described [Here: ResearchHub Bounties](https://www.researchhub.com/paper/1299105/communicative-agents-for-software-development/bounties).

ChatRnD will specialize in creating a multi-agent or team version of [PhDBot](https://github.com/DreamBrookLabs/PhDBot).

---

## A. Top 5 Priorities for Development
1. Define role structures for ChatRnD and create a new architectural blueprint.
2. Design the ChatEnv configuration and base/background system prompts.
3. Redefine ChatConfig structure and content based on roles in ChatRnD.
4. Develop basic task parsing and assignment upon receiving a user prompt for a "Research Topic"; define task termination criteria.
5. Create Wireframe design for all reports type. Test the generation (exploratory) reports based on literature findings and analyses within the research topic.

## B. Development Guideline
We envision ChatRnD to be fully open-source, and thus would be constructed with complete support for modularity in choosing LLM-Engine and DataHub Framework. A Bring your Own (LLM) Model and  Tools are also highly encouraged. Thus, we will strive for ease of import and compatibility with most commonly used framework/tools out there. This will be updated from time to time based on user-request and development priorities.

## C. Goals
### Tier I: Simple
* **Objective:** [Exploratory Research Report] Provide a 5-8 page weekly/monthly research report on a specific topic equivalent to first/second year Graduate Student.
* **Scope:** Perform literature reviews, ideate possible improvements, assess feasibility, etc.
* **Duration:** Complete the exploratory research report within 30 minutes of receiving the research topic prompt.

### Tier II: Moderate
* **Objective:** [PhD Qualification Proposal] Deliver a 10-25 page detailed analysis, similar to what to be expected of in PhD Qualification Proposal.
* **Scope:** 
  1. Detailed Background/Significance for the research
 2. ChatRnD should be capable of deriving/outlining the relevant Theory/Methods underlying the topic
 3. Produce a Specific and Feasible Research Experiment Plan as necessary, including basic settings and pro/cons when appropriate.
 4. ChatRnD must be able to provide a mock of expected research outcome, both in the context of positive or negative outcome.
 5. On top of 1-4, ChatRnD must be capable of enlist and describe the limitations/alternative approaches to what laid out in the Report.
* **Duration:** This whole process from receiving Research Topic prompt (in which intermediate **Exploratory Research Report** will be produced) to finishing the **PhD Qualification Proposal** should be *<3 hrs* of continuous operation/revisions. Termination will be imposed either if "improvement" is deemed to be negligible or the termination considerations were crossed. 

### Tier III: Complex
* **Objective:** [Final RnD Report] Prepare a reinforcement analysis based on the proposed PhD qualification proposal, including metadata analysis from research papers and in-house implementation of suggested methods.
* **Scope:**
The goal for Tier III is for ChatRnD to be able preparing a reinforcement analysis (e.g., doing calculation, using external tools) based on the proposed PhD Qualification Proposal. The Analysis will include a meta-data analysis from research paper and/or some in-house implementation of the method suggested.  Moreover, after completion of the **Final RnD Report**, ChatRnD should be integrate it's collective memory/knowledge to a [PhDBot](https://github.com/DreamBrookLabs/PhDBot) representative that will eventually present the report to human user. The presentation will be mainly a text-to-speech interaction between user and the PhDBot being "Examined". 

Ideally if the human user(s) satisfied with the explanation given, the PhDBot will then be granted full PhDBot Candidacy status. 

* **Duration:** The whole process from receiving Research Topic prompt to **Final RnD Report** (including all the intermediate output in Tier I and Tier II) is expected to be done within *<8 hrs* 

## D. Deliverables
- Public code repositories on GitHub.
- A main info page at [ChatRnD](https://chatrnd.cloud).
- An interactive app for proof-of-concept at [ChatRnD App](https://app.chatrnd.cloud).
- A gallery showcasing case studies at [ChatRnD Gallery](https://chatrnd.cloud/gallery).
- Options for self-hosted servers for user testing, development, and deployment.

## E. Future Stretch Goals
 Being able to work in a continuous way toward a full-fledge **long-form PhD dissertation** something about at least 50-100 pages long.
 The document will highlight a void/missing link in theory/method/concept within a particular research field, and work out possible novel approach or solution toward addressing it. A decent work that demonstrate how the proposed approach in action should be included. 
 The expected timeline will be for the ChatRnD to run continuously for several days up to a week or so. To then come up with the first version of the dissertation. 

---

**Special Thanks:** 
- [@Tyler Diorio](https://www.researchhub.com/user/956713/overview) (Chief of Staff at ResearchHub)
- [@Jeffrey Koury](https://www.researchhub.com/user/932947/overview) (Director at ResearchHub Foundation)

These individuals have initiated discussions and brainstorming sessions that led to the start of this open & collaborative decentralized science (DeSci) project.

**Call for Contributors:**
After the initial framework for this project is worked out we are inclined to open a call for contributors to develop scientific use-cases and training the Agents on different expertise as part of our
[ResearchPreneur Partnership Program](https://github.com/DreamBrookLabs/ResearchPreneur) (to be announced)


By DreamBrook Labs  
June 2024

 





