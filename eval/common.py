"""Shared helpers for the Haggett Hall evaluation scripts (INFO 492, GC Team 7)."""
import csv, json, re

def load_log(path="data/haggett_rfi_log_clean.csv"):
    with open(path, newline="") as f:
        return {r["rfi_id"]: r for r in csv.DictReader(f)}

def priority_from_window(days):
    """Ground-truth priority = the response window Andersen (the GC) gave each RFI.
    <=4 days -> 1 (urgent), 5-9 days -> 2, >=10 days -> 3."""
    days = int(days)
    return 1 if days <= 4 else (2 if days <= 9 else 3)

# Simple-way baseline, written down in the Evaluation Lab Worksheet on Oct 16
# (before we had the Haggett data): priority 1 if the question mentions a
# conflict or discrepancy, otherwise priority 3.
KEYWORD_RULE = re.compile(r"conflict|discrepan", re.I)

def keyword_priority(question):
    return 1 if KEYWORD_RULE.search(question) else 3

def load_results(path):
    with open(path) as f:
        return {str(r["rfi_id"]): r for r in json.load(f)}
