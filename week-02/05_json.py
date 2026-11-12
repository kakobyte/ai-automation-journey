import csv
import json
jobs = []

with open("week-02/data/jobs.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["salary"]:
            row["salary"] = int(row["salary"])
        else:
            row["salary"] = None
        row["remote"] = row["remote"].strip().lower() == "true"
        jobs.append(row)

print(f"Number of jobs: {len(jobs)}")
for job in jobs:
    print(f"{job['remote']}")

#print(jobs)

print(type(jobs[0]["salary"]))
print(type(jobs[0]["remote"]))

with open("week-02/data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=2, ensure_ascii=False)

with open("week-02/data/jobs.json", "r", encoding="utf-8") as f:
    loaded_jobs = json.load(f)

print(type(loaded_jobs[0]["salary"]))
print(type(loaded_jobs[0]["remote"]))