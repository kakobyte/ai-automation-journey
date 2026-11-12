import json
from rich import print
from helpers import parse_salary

print(parse_salary("65000"))
print(parse_salary("abc"))

with open("week-02/data/jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

print(jobs[:2])