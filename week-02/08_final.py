import csv
import json
import sys
from helpers import parse_salary

INPUT_PATH = "week-02/data/jobs_raw.csv"
OUTPUT_PATH = "week-02/data/remote_jobs.json"
MIN_SALARY = 55000

def load_jobs(path): 
    jobs = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for job in reader:
            jobs.append(job)
    return jobs

def clean_job(job):
    cleaned = dict(job)
    cleaned["salary"] = parse_salary(cleaned["salary"])
    cleaned["remote"] = cleaned["remote"].strip().lower() == "true"
    return cleaned

def filter_jobs(jobs, min_salary):
    filtered_jobs = []
    for job in jobs:
        if job["remote"] and job["salary"] is not None and job["salary"] >= min_salary:
            filtered_jobs.append(job)
    return filtered_jobs

def save_jobs(jobs, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)

try:
    raw_jobs = load_jobs(INPUT_PATH)
except FileNotFoundError:
    print(f"Datei nicht gefunden: {INPUT_PATH}")
    sys.exit(1)

jobs = [clean_job(job) for job in raw_jobs]
remote_jobs = filter_jobs(jobs, MIN_SALARY)
save_jobs(remote_jobs, OUTPUT_PATH)

print(f"{len(raw_jobs)} Jobs eingelesen")
print(f"{len(remote_jobs)} Jobs gefiltert (remote, ab {MIN_SALARY})")
print(f"Gespeichert in: {OUTPUT_PATH}")
