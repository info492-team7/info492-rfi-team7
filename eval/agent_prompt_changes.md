# Agent changes for Haggett Hall (handoff to the agent owner)

The Demo 1 prompt was written for bid-phase questions to a contracting officer. Haggett Hall RFIs
are construction-phase questions from the GC to the design team, so these lists need to change.
The scoring script expects exactly these values.

**root_cause:** `field_condition`, `design_conflict`, `missing_info`, `contractor_proposal`
(definitions in `labeling_guide.md`; drop `scope_split` and `third_party`)

**responder:** `architect`, `structural`, `civil`, `geotechnical`, `mechanical_electrical`,
`landscape`, `multiple`

**priority:** 1 = answer within about 3 days (field work waiting), 2 = about a week,
3 = about two weeks. Put these definitions in the prompt; v1 over-flagged urgency.

**due:** replace `before_proposal_due` / `next_amendment` with a number of days (3, 7 or 14).

**duplicate_of:** give the agent the earlier RFIs (`data/haggett_all_rfis.json`, only those
created before the current one) and ask for the RFI number it continues, or null.
Follow-ups in the log: 26.1 to 26, 27.1 to 27, 30.1 to 30, 30.2 to 30.1.

**Inputs:** use the full question text (no paraphrasing). Run the 10-RFI test set twice, and
all 35 RFIs once for the time model.
