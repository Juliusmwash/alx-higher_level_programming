#!/usr/bin/python3
""" Backend technical challenge """
import requests
import sys


def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit", {}).get("author", {}).get("name")
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)
