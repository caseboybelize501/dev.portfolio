import numpy as np
from sklearn.linear_model import SGDRegressor
from typing import Dict, List

class MetaLearner:
    def __init__(self):
        self.model = SGDRegressor(random_state=42)
        self.is_fitted = False
    
    def partial_fit(self, data: Dict):
        """
        Update model with new learning data
        """
        # Convert data to features
        features = [
            1.0 if data.get("portfolio_style", "default") == "technical_deep_dive" else 0.0,
            1.0 if data.get("developer_type", "unknown") == "Python" else 0.0,
            data.get("inbound_opportunity_rate", 0.0)
        ]
        
        target = data.get("inbound_opportunity_rate", 0.0)
        
        if not self.is_fitted:
            self.model.partial_fit([features], [target])
            self.is_fitted = True
        else:
            self.model.partial_fit([features], [target])
    
    def predict(self, features: List[float]) -> float:
        """
        Predict opportunity rate for given features
        """
        if not self.is_fitted:
            return 0.0
        return self.model.predict([features])[0]