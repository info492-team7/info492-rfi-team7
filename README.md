# info492-rfi-team7
INFO 492 C Construction Informatics - GC Team 7

## Project Overview

GC Team 7 is developing an AI-assisted Request for Information (RFI) triage system for construction project coordination.

Our project explores whether AI can help general contractors identify urgent RFIs earlier, route questions to appropriate responders, and reduce RFI processing delays.

Our initial thesis is that improved RFI triage could reduce processing time by approximately 10%. This remains a hypothesis that requires further validation.

## Repository Table of Contents

| Location | Description |
|---|---|
| `agent/` | AI agent code used for RFI triage |
| `data/` | RFI datasets used in the experiments |
| `eval/` | Evaluation scripts and testing materials |
| `results/` | Results from the first two demos |
| `index.html` | Web application interface |
| `script.js` | Web application functionality |
| `style.css` | Web application styling |
| `README.md` | Project overview and repository documentation |

## Demo 1: Initial RFI Triage

Our first experiment evaluated the AI agent using 10 practice RFIs.

The evaluation focused on responder assignment, priority classification, contractual risk, and identifying related RFIs.

Initial results suggested that responder routing was promising, while priority classification needed improvement.

## Demo 2: Real Construction Data

Our second experiment used real RFI records from the UW Haggett Hall construction project.

We evaluated an updated AI agent and improved the web application with interactive Ask AI and evidence review features.

The experiment highlighted the need for better priority calibration and evaluation using real construction data.

## Stakeholder Feedback

Our team conducted an interview with a construction management expert on October 29, 2026.

The interview highlighted the importance of formal RFI review processes, construction schedules, and avoiding unnecessary urgency alerts.

The complete interview transcript will be added once permission for public sharing is confirmed.

## Class Feedback

Instructor feedback emphasized three areas:

1. Demonstrating how AI triage could prevent coordination delays.
2. Aligning priority recommendations with industry practices.
3. Using real data and stakeholder feedback for evaluation.

A separate LLM feedback summary and supporting documentation will be included in the repository.

## LLM Prompts and Dependencies

The prompts, dependencies, and setup instructions used in the first two demos will be documented alongside the relevant code.

## Limitations and Next Steps

Our current evaluation does not establish that the system reduces RFI processing time by 10%.

Future work will focus on improving priority calibration, incorporating construction schedule information, and conducting user testing with construction professionals.

## Web Application

[View our web application](https://info492-team7.github.io/info492-rfi-team7/)
