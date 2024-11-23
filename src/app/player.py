from typing import Dict
import yfinance as yf
import pandas as pd


class Player:
    def __init__(self, name: str, age: int, career: str):
        self.name = name
        self.age_in_months = age * 12
        self.career = career

        # Financial attributes
        self.cash = 10000.0
        self.investments: Dict[str, float] = {}
        self.investments_value = 0.0
        self.real_estate_value = 0.0
        self.monthly_income = self._initialize_income()
        self.monthly_expenses = 2000.0  # TODO: Use real data based on inflation

        # Historical data
        self.salary_history = [self.monthly_income]
        self.networth_history = [self.net_worth]
        self.cash_history = [self.cash]

        # Stats
        self.happiness = 100
        self.health = 100
        self.education = 50

    # TODO: use real data, make it more realistic... enterpreneur should have more variable income, even negative. Employee should be based on type of job
    def _initialize_income(self) -> float:
        if self.career == "Student":
            return 1500.0
        elif self.career == "Employee":
            return 4000.0
        else:  # Entrepreneur
            return 3000.0

    @property
    def net_worth(self) -> float:
        return self.cash + self.investments_value + self.real_estate_value

    def invest(self, amount: float) -> bool:
        if amount <= self.cash:
            self.cash -= amount
            # Simulate investment in S&P 500
            self.investments_value += amount
            return True
        return False

    def spend_money(self, amount: float, category: str) -> bool:
        if amount <= self.cash:
            self.cash -= amount
            return True
        return False

    def earn_money(self, amount: float):
        self.cash += amount

    def change_job(self, salary_increase: float):
        self.monthly_income *= salary_increase

    def advance_month(self):
        # Monthly income
        self.earn_money(self.monthly_income)

        # Monthly expenses
        self.spend_money(self.monthly_expenses, "living_expenses")

        self.age_in_months += 1

        # Update investments value
        self._update_investments()

        # Update historical data
        self.salary_history.append(self.monthly_income)
        self.networth_history.append(self.net_worth)
        self.cash_history.append(self.cash)

    def _update_investments(self):
        if self.investments_value > 0:
            # Simulate average market return
            # TODO: Use real market data
            monthly_return = 0.007  # About 8.4% annually
            self.investments_value *= 1 + monthly_return
