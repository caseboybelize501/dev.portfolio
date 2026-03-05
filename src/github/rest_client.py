import httpx
import asyncio
from typing import List, Dict

class GitHubRESTClient:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.client = httpx.AsyncClient(base_url=self.base_url)
    
    async def get_user_repos(self, username: str) -> List[Dict]:
        """
        Get user repositories
        """
        try:
            response = await self.client.get(f"/users/{username}/repos")
            return response.json()
        except Exception as e:
            print(f"Error fetching repos: {e}")
            return []
    
    async def get_user_events(self, username: str) -> List[Dict]:
        """
        Get user events
        """
        try:
            response = await self.client.get(f"/users/{username}/events")
            return response.json()
        except Exception as e:
            print(f"Error fetching events: {e}")
            return []
    
    async def get_user_starred(self, username: str) -> List[Dict]:
        """
        Get user starred repositories
        """
        try:
            response = await self.client.get(f"/users/{username}/starred")
            return response.json()
        except Exception as e:
            print(f"Error fetching starred repos: {e}")
            return []