import stripe
from typing import Dict, List

stripe.api_key = "sk_test_..."  # In production, use environment variable

class StripeGate:
    def __init__(self):
        pass
    
    async def create_checkout_session(self, tier: str) -> str:
        """
        Create Stripe checkout session for subscription
        """
        try:
            # Define tiers
            tiers = {
                "dev": 900,  # $9/month in cents
                "growth": 2900,  # $29/month in cents
                "agency": 5000  # $50/month in cents
            }
            
            price_id = tiers.get(tier)
            if not price_id:
                raise ValueError(f"Invalid tier: {tier}")
            
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price": price_id,
                    "quantity": 1,
                }],
                mode="subscription",
                success_url="https://dev.portfolio/app/success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="https://dev.portfolio/app/cancel",
            )
            
            return session.url
        except Exception as e:
            print(f"Error creating checkout session: {e}")
            return ""