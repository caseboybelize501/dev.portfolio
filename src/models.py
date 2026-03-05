from pydantic import BaseModel
from typing import List, Dict, Optional

class TechIdentity(BaseModel):
    primary_languages: List[str]
    domain_expertise: List[str]
    specialty_signals: List[str]
    collaboration_style: str
    depth_vs_breadth_index: float
    standout_projects: List[Dict]
    recommended_portfolio_style: str
    memory_pattern_used: Optional[str]

class SkillsGraph(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]
    metadata: Dict

class RecruiterBrief(BaseModel):
    developer: str
    achievements: List[str]
    tech_stack: List[str]
    project_impact: str
    availability: str
    contact: str

class Portfolio(BaseModel):
    title: str
    content: str
    style: str
    projects: List[Dict]
    skills: SkillsGraph

class SystemProfile(BaseModel):
    models: List[Dict] = []
    inference_config: Dict = {}
    tools: Dict = {}
    static_sites: Dict = {}
    ports: List[int] = []