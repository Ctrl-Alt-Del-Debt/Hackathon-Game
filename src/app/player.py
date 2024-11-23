from app.salaries_data_preprocessing import MzdyData
from src.constants.data_constants import (
    FILE_PATH_SALARIES,
    STARTING_YEAR,
    CAREERS_LIST,
    STUDENT_INCOME,
    STARTING_AGE,
    FILE_PATH_INFLATION,
    STARTING_RENT,
    STARTING_ADDITIONAL_EXPENSES,
)

from typing import Dict
import yfinance as yf
import pandas as pd


class Player:
    def __init__(self, name: str, age: int, career: str, region="Jihomoravský kraj"):
        self.name = name
        self.age_in_months = age * 12
        self.current_year = STARTING_YEAR + (self.age_in_months * 12 - STARTING_AGE)
        self.career = career
        self.region = (
            region  # default region is JMK but can be changed to "Hlavní město Praha"
        )
        self.income_data = MzdyData(FILE_PATH_SALARIES).process_adjustments()

        # Financial attributes
        self.cash = 10000.0
        self.investments: Dict[str, float] = {}
        self.investments_value = 0.0
        self.real_estate_value = 0.0
        # self.monthly_income = self._initialize_income()
        # self.additional_expenses = self._compute_additional_expenses()
        # self.monthly_rent_expenses = self._compute_monthly_rent_expenses()

        self.monthly_income = 300
        self.additional_expenses = 200
        self.monthly_rent_expenses = 100

        # Historical data
        self.salary_history = [self.monthly_income]
        self.expenses_history = [self.additional_expenses]
        self.rent_history = [self.monthly_rent_expenses]
        self.networth_history = [self.net_worth]
        self.cash_history = [self.cash]

        # Events
        self.events = []

        # Stats
        self.happiness = 100
        self.health = 100
        self.education = 50
        self.is_married = False
        self.childern = 0
        self.property = []

    def _compute_monthly_rent_expenses(self) -> float:
        if self.current_year == STARTING_YEAR:
            return STARTING_RENT
        else:
            inflation_data = pd.read_excel(FILE_PATH_INFLATION)
            inflation_data_filtered = inflation_data[
                inflation_data["Rok"] == self.current_year
            ]
            inflation_rate = (
                inflation_data_filtered["Bydlení, voda, energie,\npaliva"]
                .iloc[0]
                .item()
            )
            return self.monthly_rent_expenses + (
                self.monthly_rent_expenses * inflation_rate
            )

    def _compute_additional_expenses(self) -> float:
        if self.current_year == STARTING_YEAR:
            return STARTING_ADDITIONAL_EXPENSES
        else:
            inflation_data = pd.read_excel(FILE_PATH_INFLATION)
            inflation_data_filtered = inflation_data[
                inflation_data["Rok"] == self.current_year
            ]
            inflation_rate = inflation_data_filtered["Úhrn"].iloc[0].item()
            return self.additional_expenses + (
                self.additional_expenses * inflation_rate
            )

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
                    (self.income_data["Rok"] == str(self.current_year))
                    & (self.income_data["ČR, kraje"] == self.region)
                ]
                income = income_data_filtered[self.career].iloc[0].item()
                return int(income)
            elif self.career == "Student":
                return int(STUDENT_INCOME)
        except:
            print(
                "Something went wrong during an income settings."
            )  # TODO: logging should be implemented instead printing

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

    def advance_month(self, engine):
        # Monthly income
        self.earn_money(self.monthly_income)

        # Monthly expenses
        self.spend_money(
            self.additional_expenses + self.monthly_rent_expenses, "living_expenses"
        )

        # Age one month
        self.age_in_months += 1

        # Update investments value
        self._update_investments()

        # Update historical data
        self.salary_history.append(self.monthly_income)
        self.networth_history.append(self.net_worth)
        self.cash_history.append(self.cash)
        self.expenses_history.append(self.additional_expenses)
        self.rent_history.append(self.monthly_rent_expenses)

        self.events.append(engine.get_current_event())

    def _update_investments(self):
        if self.investments_value > 0:
            # Simulate average market return
            # TODO: Use real market data
            monthly_return = 0.007  # About 8.4% annually
            self.investments_value *= 1 + monthly_return

    def buy_a_property(self, property):
        if self.cash >= property.price:
            print("you have enough money to buy a property.")
            self.cash -= property.price
            self.property.append(property)
        else:
            raise Exception("Not enough money.")

    def sell_all_investments(self):
        self.cash += self.investments_value
        self.investments_value = 0

    def child_born(self):
        self.childern += 1
