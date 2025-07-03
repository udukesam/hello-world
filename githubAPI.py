import requests

# Replace with your values
GITHUB_TOKEN = "your_personal_access_token"
REPO_OWNER = "your-org-or-username"
REPO_NAME = "your-repo-name"

# API endpoint to list recent commits
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"

# Headers with authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Make the request
response = requests.get(url, headers=headers)

# Parse the response
if response.status_code == 200:
    commits = response.json()
    for commit in commits:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        message = commit["commit"]["message"]
        date = commit["commit"]["author"]["date"]
        print(f"Commit: {sha}\nAuthor: {author}\nDate: {date}\nMessage: {message}\n{'-'*40}")
else:
    print("Error:", response.status_code, response.text)
