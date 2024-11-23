from app.salaries_data_preprocessing import MzdyData
from src.constants.data_constants import FILE_PATH_SALARIES, STARTING_YEAR, CAREERS_LIST, STUDENT_INCOME, STARTING_AGE

from typing import Dict
import yfinance as yf
import pandas as pd


class Player:
    def __init__(self, name: str, age: int, career: str, region = "Jihomoravský kraj"):
        self.name = name
        self.age = age
        self.current_year = STARTING_YEAR + (self.age - STARTING_AGE)
        self.career = career
        self.region = region  # default region is JMK but can be changed to "Hlavní město Praha"
        self.income_data = MzdyData(FILE_PATH_SALARIES).process_adjustments()

        # Financial attributes
        self.cash = 10000.0
        self.investments: Dict[str, float] = {}
        self.investments_value = 0.0
        self.real_estate_value = 0.0
        self.monthly_income = self._initialize_income()
        self.monthly_expenses = 2000.0  # TODO: Use real data based on inflation
        #self.monthly_expenses = self._compute_monthly_expenses()

        # Historical data
        self.salary_history = [self.monthly_income]
        self.networth_history = [self.net_worth]
        self.cash_history = [self.cash]

        # Stats
        self.happiness = 100
        self.health = 100
        self.education = 50
        self.months = 0  # Initialize month counter
    
    def _compute_monthly_expenses(self) -> int:
        pass

    
    # TODO: hardcoded start in 20 year -> should be changed
    def _initialize_income(self) -> int:
        """
        Initialize income based on age, career, and data from the income data.
        Calculate the year which should be used based on age:
            e.g. age 20 --> 2006 / age 21 --> 2007
        """
        try:
            if self.career in CAREERS_LIST:
                income_data_filtered = self.income_data[
                    (self.income_data['Rok'] == str(self.current_year)) &
                    (self.income_data['ČR, kraje'] == self.region)
                ]
                income = income_data_filtered[self.career].iloc[0].item()
                return int(income)
            elif self.career == "Student":
                return int(STUDENT_INCOME)
        except:
            print("Something went wrong during an income settings.")        # TODO: logging should be implemented instead printing
        
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

        # Age one month
        self.months += 1
        if self.months >= 12:
            self.age += 1
            self.months = 0

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
