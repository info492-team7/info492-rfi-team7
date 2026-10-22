# Evaluation (Demo 2): Haggett Hall

Run from the repo root. Python 3, no extra packages.

```
python eval/time_model.py                         # baseline + perfect-flag and keyword scenarios
python eval/score_agent.py results/run1.json results/run2.json
python eval/time_model.py results/run_all35.json  # time effect of the real agent
```

1. **Answer key** (`data/answer_key.csv`). Priority, urgency, responder, follow-up and impact
   come from the log itself. Root cause is the only field people label: two teammates fill
   `root_cause_labeler_A` and `_B` separately (using `labeling_guide.md`), then agree on
   `root_cause_final`. They also guess priority from the text alone, which shows how hard the
   task is for a person.
2. **Agent runs.** Run the agent twice on `data/rfi_test_set.json` and save each output.
   Also run it once on `data/haggett_all_rfis.json` for the time model.
3. **Simple way.** Built into `score_agent.py`: the keyword rule we wrote down on Oct 16
   (conflict or discrepancy = priority 1, otherwise 3), and "send everything to the architect".
4. **Time model.** Baseline is the actual log. The agent scenario assumes a flagged urgent RFI
   that was late gets answered by its due date (full effect) or half as late (half effect).
   False alarms shrink the effect. See the docstring in `time_model.py`.
