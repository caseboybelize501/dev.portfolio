import httpx
import asyncio
from typing import Dict, List

class GitHubGraphQLClient:
    def __init__(self):
        self.base_url = "https://api.github.com/graphql"
        self.client = httpx.AsyncClient(base_url=self.base_url)
    
    async def get_contributions(self, username: str) -> Dict:
        """
        Get 52-week contribution graph via GraphQL
        """
        query = """
        query($username: String!) {
          user(login: $username) {
            contributionsCollection {
              contributionCalendar {
                weeks {
                  contributionDays {
                    date
                    contributionCount
                  }
                }
              }
            }
          }
        }
        """
        
        try:
            response = await self.client.post(
                self.base_url,
                json={
                    "query": query,
                    "variables": {"username": username}
                }
            )
            return response.json()
        except Exception as e:
            print(f"Error fetching contributions: {e}")
            return {}