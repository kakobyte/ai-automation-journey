job = {
    "title": "Software Engineer",
    "company": "TechCorp",
    "city": "San Francisco",
    "salary": 120000,
    "remote": True
}

print(job["title"])

job["salary"] = 130000
job["skills"] = ["Python", "JavaScript", "SQL"]

print(f"Salary: ${job['salary']:,}, Skills: {job['skills']}")

print(f"Contact: {job.get('contact', 'Not provided')}")

for key, value in job.items():
    print(f"{key}: {value}")