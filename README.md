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


The initial scoring approach awards one point per matched preference. It is a simple comparison heuristic, not a validated measure of fairness. Essential requirements are checked before preference scoring.
Technology
- Python
- LangChain
- A model provider that supports tool calling (to be selected)
- python-dotenv for environment configuration
- JSON for local decision storage

The first version uses user-supplied options with shared attributes such as cost, duration, and tags. It does not retrieve live prices or listings, make bookings, or guarantee that a group will agree. When requirements conflict, the assistant should explain the conflict and ask what can change rather than silently relaxing a requirement.
Planned demo checks
- Several feasible options with different preference scores.
- No option satisfying every essential requirement.
- An option missing an attribute needed for evaluation.
- Updated preferences triggering a new comparison.
- A decision saved only when requested.
Inspiration
This project applies the tool-calling concepts introduced in IBM's LangChain agent tutorial. Implementation will follow the current LangChain documentation.
