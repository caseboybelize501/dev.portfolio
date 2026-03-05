import json
from typing import Dict, List

class IdentityPatternStore:
    def __init__(self, file_path="identity_patterns.json"):
        self.file_path = file_path
        self.patterns = self._load()
    
    def _load(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.patterns, f, indent=2)
    
    def add_pattern(self, identity_pattern: Dict, language_combination: List[str], domain_signals: List[str]):
        pattern = {
            "identity_pattern": identity_pattern,
            "language_combination": language_combination,
            "domain_signals": domain_signals,
            "timestamp": "2026-01-01T00:00:00Z"
        }
        self.patterns.append(pattern)
        self.save()
    
    def get_all_patterns(self) -> List[Dict]:
        return self.patterns
    
    def query_patterns(self, opportunity_type: str) -> List[Dict]:
        # Placeholder for pattern querying logic
        return [p for p in self.patterns if "opportunity" in str(p)]