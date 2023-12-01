#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest) of the "rails" repository by the user "rails" on GitHub.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = "rails"
    owner_name = "rails"

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(url)
        commits = response.json()

        if response.status_code == 200:
            for commit in commits[:10]:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f'{sha}: {author_name}')
        else:
            print(f"Error: Unable to fetch commits. HTTP Status Code: {response.status_code}")

    except ValueError:
        print("Error: Not a valid JSON. Check your repository and owner names.")

