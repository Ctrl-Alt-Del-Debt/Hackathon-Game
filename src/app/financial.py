import yfinance as yf
import pandas as pd
from typing import Dict, List, Tuple


class FinancialMarket:
    def __init__(self):
        self.sp500 = self._load_sp500_data()
        self.interest_rate = 0.05  # 5% annual interest rate

    def _load_sp500_data(self) -> pd.DataFrame:
        try:
            sp500 = yf.download("^GSPC", start="2010-01-01", progress=False)
            return sp500
        except Exception:
            # Fallback to mock data if API fails
            return pd.DataFrame({"Close": [1000 * (1 + 0.07) ** i for i in range(100)]})

    def get_market_return(self, start_date: str, end_date: str) -> float:
        data = self.sp500.loc[start_date:end_date]
        return (data["Close"][-1] / data["Close"][0]) - 1

    def calculate_loan_payment(self, principal: float, years: int) -> float:
        monthly_rate = self.interest_rate / 12
        num_payments = years * 12
        return (
            principal
            * (monthly_rate * (1 + monthly_rate) ** num_payments)
            / ((1 + monthly_rate) ** num_payments - 1)
        )
