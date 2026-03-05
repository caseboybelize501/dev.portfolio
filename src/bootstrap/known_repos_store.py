import json
from pathlib import Path

class KnownReposStore:
    def __init__(self, file_path="known_repos.json"):
        self.file_path = file_path
        self.repos = self._load()
    
    def _load(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.repos, f, indent=2)
    
    def add_repo(self, username: str, repo_name: str, last_synced: str):
        if username not in self.repos:
            self.repos[username] = {}
        self.repos[username][repo_name] = {
            "last_synced": last_synced
        }
        self.save()
    
    def get_repo(self, username: str, repo_name: str):
        return self.repos.get(username, {}).get(repo_name)
    
    def get_user_repos(self, username: str):
        return self.repos.get(username, {})