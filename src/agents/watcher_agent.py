import asyncio
from typing import List, Dict
from src.github.rest_client import GitHubRESTClient
from src.github.graphql_client import GitHubGraphQLClient

class WatcherAgent:
    def __init__(self, rest_client: GitHubRESTClient, gql_client: GitHubGraphQLClient):
        self.rest_client = rest_client
        self.gql_client = gql_client
    
    async def fetch_activities(self, username: str) -> List[Dict]:
        """
        Fetch all GitHub activities for a user
        """
        print(f"Fetching activities for {username}...")
        
        # Get repos
        repos = await self.rest_client.get_user_repos(username)
        
        # Get events
        events = await self.rest_client.get_user_events(username)
        
        # Get starred repos
        starred = await self.rest_client.get_user_starred(username)
        
        # Get contribution graph via GraphQL
        contributions = await self.gql_client.get_contributions(username)
        
        # Combine all activities
        activities = {
            "repos": repos,
            "events": events,
            "starred": starred,
            "contributions": contributions
        }
        
        print(f"Fetched {len(events)} events for {username}")
        return activities