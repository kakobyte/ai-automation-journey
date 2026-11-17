import requests
import sys

url = "https://api.github.com/users/octocat/repos?per_page=3"

try:
    response = requests.get(url, timeout=10) # 5-10 sekunden sind ok
except requests.exceptions.RequestException as e:
    print(f"Der Request konnte nicht ausgeführt werden: {e}")
    sys.exit(1)
status_code = response.status_code
if status_code != 200:
    print(f"StatusCode ist {status_code}")
    sys.exit(1)
data = response.json()
for repo in data:
    print(f"{repo['name']}: {repo['stargazers_count']} Sterne")
