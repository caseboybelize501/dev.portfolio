from pydantic import BaseModel
from typing import List, Dict, Optional

class SystemProfile(BaseModel):
    models: List[Dict] = []
    inference_config: Dict = {}
    tools: Dict = {}
    static_sites: Dict = {}
    ports: List[int] = []