# Haggett Hall RFI data (Demo 2 onward)

**Source:** RFI log for UW Haggett Hall (Andersen Construction job AWA-2300), shared with
GC Team 7 by Connor McCabe (Project Engineer, Andersen Construction) on Oct 19, 2026, through
Greg Wojcicki (Construction Manager, UW Facilities Project Delivery Group). Shared for a
UW course project only. Real data, not synthetic.

**What we have:** RFIs #25 to #55 (35 RFIs, including follow-ups like 26.1 and 30.1), created
Feb 12 to Apr 9, 2025. These are pages 4 to 6 of a 42-page log. RFI 55 is cut off at the end
of page 6, so its response text is incomplete.

| File | What it is |
|---|---|
| `haggett_rfi_log_clean.csv` | All 35 RFIs parsed from the PDF, one row each, with derived timing fields |
| `haggett_all_rfis.json` | ID, created date and question for all 35 (agent input, and context for catching follow-ups) |
| `rfi_test_set.json` | The 10 RFIs we evaluate on (same format the triage agent already reads) |
| `answer_key.csv` | Ground truth for the 10, plus blank columns for the two labelers |

## Columns in `haggett_rfi_log_clean.csv`

| Column | Meaning |
|---|---|
| `rfi_id` | RFI number from the log (e.g. 30.1) |
| `parent_rfi` | For follow-ups like 30.1, the RFI they continue (30) |
| `is_followup`, `references_rfi` | Y if the RFI continues or cites an earlier RFI in the log |
| `question` | Full question text |
| `assignees`, `official_responder` | People the RFI went to, and who gave the official answer |
| `cost_impact`, `schedule_impact` | As recorded in the log (Yes / No / TBD / Blank) |
| `created`, `due` | Dates from the log |
| `first_response`, `last_response` | Earliest and latest response dates in the log |
| `due_variance_days` | The log's own Due Date Variance (negative = early) |
| `closed_derived` | `due + due_variance_days`. Matches `last_response` for 24 of 35 RFIs; for the rest the RFI was closed a few days after the last response |
| `response_window_days` | `due - created`: how long Andersen gave the design team. We use this as the GC's own urgency rating |
| `days_open` | `closed_derived - created`. **Our processing-time measure** |
| `days_to_last_response` | `last_response - created` (a secondary measure) |
| `late` | Y if closed after the due date |

## Urgency from the response window

Andersen gave each RFI a due date. The windows fall into three clear groups, which we use as
priority ground truth:

| Window | Priority | RFIs |
|---|---|---|
| 2 to 4 days | 1 (urgent) | 12 |
| 7 to 9 days | 2 | 7 |
| 13 to 27 days | 3 | 16 |
