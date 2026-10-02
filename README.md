CommonGround
A conversational group decision assistant built as a Python and LangChain learning project.
CommonGround explores how an AI agent can help people choose between shared options by collecting preferences, checking essential requirements, and explaining trade-offs. It is designed for decisions such as choosing an activity, meal, movie, or team project.
Status: Early-stage proof of concept. The capabilities below describe the planned MVP; implementation is in progress.

The idea
Group decisions often involve conflicting preferences. One person prefers an outdoor activity, another needs an indoor venue, and someone else has a strict budget. CommonGround aims to distinguish requirements that must be met from preferences that can be balanced.
Users supply the candidate options and each participant's requirements. The agent coordinates Python tools to evaluate those options and explain the result.
Planned MVP
- Collect options, participant constraints, and preferences through conversation.
- Check budgets, duration limits, and required attributes.
- Rank feasible options using a transparent preference-matching rule.
- Explain rejected options and individual trade-offs.
- Ask for missing information and identify conflicting requirements.
- Reevaluate options when preferences change.
- Save the selected decision to a local JSON file when requested.
- Display tool calls to make the agent workflow observable.
Example scenario
Options
Option	Cost per person (PKR)	Duration	Setting
Cinema	1,200	2 hours	Indoor
Bowling	1,800	1 hour	Indoor
Picnic	500	3 hours	Outdoor


Participants
- Ayesha: maximum budget of PKR 1,500; prefers outdoors.
- Sara: requires an indoor activity; prefers a shorter duration.
- Ali: maximum budget of PKR 2,000; prefers cinema.
Expected result
Cinema is the only feasible option: bowling exceeds Ayesha's budget, and the picnic violates Sara's indoor requirement. The explanation should acknowledge that Ayesha's outdoor preference is not satisfied.
These are sample options and prices, not live listings.
How it is designed to work
1. The model interprets the user's request and collects missing details.
2. The agent calls check_constraints to evaluate essential requirements.
3. If feasible candidates remain, it calls score_options to compare preferences.
4. The model explains the computed results and trade-offs.
5. On request, save_decision records the selected option.
The model handles conversation and tool selection. Python functions perform filtering and scoring. LangChain coordinates model calls and tool execution.
Planned tools
Tool	Responsibility
check_constraints	Identify feasible candidates and provide reasons for rejection or missing information.
score_options	Return individual and group preference scores for feasible candidates.
save_decision	Write a selected decision to a local JSON file.


The initial scoring approach awards one point per matched preference. It is a simple comparison heuristic, not a validated measure of fairness. Essential requirements are checked before preference scoring.
Technology
- Python
- LangChain
- A model provider that supports tool calling (to be selected)
- python-dotenv for environment configuration
- JSON for local decision storage
Initial setup
Create and activate a virtual environment with Python 3.10 or newer:
python -m venv .venv
Linux/macOS:
source .venv/bin/activate
Windows PowerShell:
.\.venv\Scripts\Activate.ps1
Install the base dependencies:
python -m pip install -U langchain python-dotenv
Provider-specific dependencies, credential configuration, and the application launch command will be added once the model integration and CLI are implemented. Keep API credentials in environment variables or an untracked .env file. Exclude .env and .venv/ from Git.
Learning goals
- Understand the difference between calling a model and running an agent.
- Expose Python functions as tools with structured inputs.
- Observe how tool results feed into later model calls.
- Handle missing information, infeasible requests, and tool failures.
- Maintain context across follow-up messages.
- Keep calculation logic inspectable and separate from generated explanations.
Scope and limitations
The first version uses user-supplied options with shared attributes such as cost, duration, and tags. It does not retrieve live prices or listings, make bookings, or guarantee that a group will agree. When requirements conflict, the assistant should explain the conflict and ask what can change rather than silently relaxing a requirement.
Planned demo checks
- Several feasible options with different preference scores.
- No option satisfying every essential requirement.
- An option missing an attribute needed for evaluation.
- Updated preferences triggering a new comparison.
- A decision saved only when requested.
Inspiration
This project applies the tool-calling concepts introduced in IBM's LangChain agent tutorial. Implementation will follow the current LangChain documentation.
