# info492-rfi-team7
INFO 492 C Construction Informatics - GC Team 7

## RFI Triage Agent

This project uses Python and the Gemini API to analyze construction RFIs. The agent identifies root causes, assigns priorities, evaluates contractual risks, and suggests responders.

We tested the agent on 10 RFIs and saved the results in `data/agent_results.json`.

## LLM Prompts Used

We used the Gemini 3.1 Flash-Lite model to analyze RFIs.

The prompt asks the model to:
- Identify the root cause of each RFI
- Determine whether a response is needed
- Identify the appropriate responder and due date
- Evaluate contractual risk and explain the reason
- Assign priority (1 = high, 2 = medium, 3 = low)
- Identify possible duplicate RFIs

The full prompt is available in `agent/triage_agent.py`, inside the `triage_rfi()` function.

## Dependencies

- Python
- google-genai

To install the required package:

    python -m pip install -r requirements.txt

## How to Run

Set your `GEMINI_API_KEY` environment variable before running the agent. Do not include your API key in the repository.

From the project root, run:

    python -u agent/triage_agent.py

The agent reads `data/rfi_test_set.json` and saves its outputs to `data/agent_results.json`.
