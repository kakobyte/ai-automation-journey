jobs = [
    {
        "title": "Software Engineer",
        "company": "TechCorp",
        "city": "San Francisco",
        "salary": 120000,
        "remote": True
    },
    {
        "title": "Software Engineer",
        "company": "TechCorp",
        "city": "New York",
        "salary": 110000,
        "remote": False
    },
    {
        "title": "Data Scientist",
        "company": "DataInc",
        "city": "Los Angeles",
        "remote": True
    },
    {
        "title": "Sales Associate",
        "company": "SalesCo",
        "city": "Chicago",
        "salary": 60000,
        "remote": False
    }
]    

print(f"Number of jobs: {len(jobs)}")

for job in jobs:    
    print(f"Title: {job['title']}")

remote_jobs = []
for job in jobs:
    if job.get("remote"):
        remote_jobs.append(job)

print(f"Number of remote jobs: {len(remote_jobs)}")

salaries = []
for job in jobs:
    if job.get("salary"):
        salaries.append(job["salary"])

print(f"Erste Version: Das Durchschnittsgehalt beträgt: {sum(salaries) / len(salaries):,.2f}")

total = 0
count = 0
for job in jobs:
    if job.get("salary"):
        total += job["salary"]
        count += 1

print(f"Zweite Version: Das Durchschnittsgehalt beträgt: {total / count:,.2f}")

best_job = None
highest_salary = 0
for job in jobs:
    if "salary" in job and job["salary"] > highest_salary:
        highest_salary = job["salary"]
        best_job = job

if best_job:
    print(f"Der Job mit dem höchsten Gehalt ist: {best_job['title']} bei {best_job['company']}")