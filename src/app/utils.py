import random
from typing import List, Tuple

def generate_random_event() -> Tuple[str, List[str]]:
    events = [
        ("Job Loss", ["Look for a new job", "Start a business", "Take temporary work"]),
        ("Market Crash", ["Hold investments", "Sell everything", "Buy the dip"]),
        ("Inheritance", ["Invest it all", "Save for later", "Spend on education"]),
        ("Health Issue", ["Use insurance", "Pay from savings", "Take a loan"]),
    ]
    return random.choice(events)

def calculate_happiness(financial_status: float, health: float, social: float) -> float:
    weights = [0.4, 0.3, 0.3]
    return (
        financial_status * weights[0] +
        health * weights[1] +
        social * weights[2]
    )

def format_currency(amount: float) -> str:
    return f"${amount:,.2f}"

def calculate_risk_score(age: int, savings: float, income: float) -> float:
    base_score = 100 - age
    savings_factor = min(savings / (income * 5), 1)
    return base_score * savings_factor
