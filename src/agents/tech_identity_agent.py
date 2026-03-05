import json
from typing import List, Dict
from src.memory.identity_pattern_store import IdentityPatternStore

class TechIdentityAgent:
    def __init__(self, identity_store: IdentityPatternStore):
        self.identity_store = identity_store
    
    async def analyze(self, activities: Dict) -> Dict:
        """
        Analyze technical identity from GitHub activity
        """
        print("Analyzing technical identity...")
        
        # Simulate LLM analysis with prompt pattern
        prompt = self._build_prompt(activities)
        
        # In a real implementation, this would call an LLM
        # For now, we'll simulate the response
        tech_identity = {
            "primary_languages": ["Python", "JavaScript"],
            "domain_expertise": ["Backend Development", "Data Science"],
            "specialty_signals": ["Deep Code Reviews", "Open Source Contributions"],
            "collaboration_style": "Collaborative",
            "depth_vs_breadth_index": 0.75,
            "standout_projects": [
                {
                    "repo": "awesome-project",
                    "reason": "High impact contributions"
                }
            ],
            "recommended_portfolio_style": "Technical Deep Dive",
            "memory_pattern_used": "similar_developer_patterns"
        }
        
        # Store in memory
        self.identity_store.add_pattern(
            identity_pattern=tech_identity,
            language_combination=tech_identity["primary_languages"],
            domain_signals=tech_identity["domain_expertise"]
        )
        
        return tech_identity
    
    def _build_prompt(self, activities: Dict) -> str:
        """
        Build prompt for LLM analysis
        """
        repos = activities.get("repos", [])
        contributions = activities.get("contributions", {})
        
        prompt = f"Synthesize a developer's technical identity from their GitHub activity."
        prompt += f"Repos: {json.dumps(repos[:5])}"
        prompt += f"Contribution graph: {json.dumps(contributions)}"
        prompt += "MEMORY — identity patterns for developers with similar activity: [IDENTITY_MEMORY]"
        prompt += "MEMORY — which signals most predict strong technical reputation: [SIGNAL_MEMORY]"
        
        return prompt