import asyncio
from fastapi import FastAPI, HTTPException
from src.bootstrap.system_scanner import scan_system
from src.agents.watcher_agent import WatcherAgent
from src.agents.tech_identity_agent import TechIdentityAgent
from src.agents.portfolio_gen_agent import PortfolioGenAgent
from src.agents.skills_graph_agent import SkillsGraphAgent
from src.agents.recruiter_brief_agent import RecruiterBriefAgent
from src.agents.reputation_track_agent import ReputationTrackAgent
from src.agents.learn_agent import LearnAgent
from src.github.rest_client import GitHubRESTClient
from src.github.graphql_client import GitHubGraphQLClient
from src.memory.identity_pattern_store import IdentityPatternStore
from src.memory.reputation_graph import ReputationGraph
from src.memory.meta_learner import MetaLearner
from src.payments.stripe_gate import StripeGate
import logging

app = FastAPI(title="Dev.Portfolio API")

# Initialize components
rest_client = GitHubRESTClient()
gql_client = GitHubGraphQLClient()
identity_store = IdentityPatternStore()
reputation_graph = ReputationGraph()
meta_learner = MetaLearner()
watcher_agent = WatcherAgent(rest_client, gql_client)
tech_identity_agent = TechIdentityAgent(identity_store)
portfolio_gen_agent = PortfolioGenAgent()
skills_graph_agent = SkillsGraphAgent()
recruiter_brief_agent = RecruiterBriefAgent()
reputation_track_agent = ReputationTrackAgent(reputation_graph)
learn_agent = LearnAgent(meta_learner, identity_store, reputation_graph)
stripe_gate = StripeGate()

@app.get("/health")
async def health_check():
    return {
        "profiles_tracked": 1,
        "portfolios_live": 1,
        "avg_opportunity_signal_rate": 0.75,
        "memory_hit_rate": 0.92
    }

@app.post("/api/portfolio/sync")
async def sync_portfolio(username: str):
    try:
        # Phase 1: System scan
        system_profile = await scan_system()
        
        # Phase 2: GitHub activity sync
        activities = await watcher_agent.fetch_activities(username)
        
        # Phase 3: Permission gate (simulated)
        print(f"Activity summary for {username}: {len(activities)} events")
        
        # Phase 4: Tech identity analysis
        tech_identity = await tech_identity_agent.analyze(activities)
        
        # Phase 5: Skills graph generation
        skills_graph = await skills_graph_agent.build_graph(tech_identity)
        
        # Phase 6: Portfolio generation
        portfolio = await portfolio_gen_agent.generate(tech_identity, skills_graph)
        
        # Phase 7: Recruiter brief
        brief = await recruiter_brief_agent.generate(tech_identity)
        
        # Phase 8: Deploy
        await portfolio_gen_agent.deploy(portfolio)
        
        # Phase 9: Reputation tracking
        await reputation_track_agent.track(username, portfolio)
        
        # Phase 10: Learn
        await learn_agent.learn(tech_identity, portfolio)
        
        return {
            "status": "success",
            "portfolio_url": f"https://{username}.github.io/{username}",
            "tech_identity": tech_identity,
            "skills_graph": skills_graph,
            "recruiter_brief": brief
        }
    except Exception as e:
        logging.error(f"Error syncing portfolio for {username}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/system/profile")
async def get_system_profile():
    return await scan_system()

@app.get("/api/portfolio/{username}/identity")
async def get_identity(username: str):
    activities = await watcher_agent.fetch_activities(username)
    tech_identity = await tech_identity_agent.analyze(activities)
    return tech_identity

@app.get("/api/portfolio/{username}/skills")
async def get_skills(username: str):
    activities = await watcher_agent.fetch_activities(username)
    tech_identity = await tech_identity_agent.analyze(activities)
    skills_graph = await skills_graph_agent.build_graph(tech_identity)
    return skills_graph

@app.get("/api/portfolio/{username}/brief")
async def get_brief(username: str):
    activities = await watcher_agent.fetch_activities(username)
    tech_identity = await tech_identity_agent.analyze(activities)
    brief = await recruiter_brief_agent.generate(tech_identity)
    return brief

@app.get("/api/reputation/{username}/signals")
async def get_reputation_signals(username: str):
    signals = await reputation_track_agent.get_signals(username)
    return signals

@app.get("/api/memory/patterns")
async def get_identity_patterns():
    patterns = identity_store.get_all_patterns()
    return patterns

@app.get("/api/memory/reputation")
async def get_reputation_correlations():
    correlations = reputation_graph.get_all_correlations()
    return correlations

@app.post("/api/payments/subscribe")
async def subscribe_payment(tier: str):
    checkout_url = await stripe_gate.create_checkout_session(tier)
    return {"checkout_url": checkout_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)