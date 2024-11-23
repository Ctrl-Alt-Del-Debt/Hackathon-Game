from dataclasses import dataclass
from typing import List, Callable, Optional, Any
from src.app.player import Player
import random
from enum import Enum


class SpendingCategory(Enum):
    EDUCATION = "education"
    WEDDING = "wedding"
    CERTIFICATION = "certification"
    PROPERTY_PURCHASE = "property_purchase"
    FAMILY = "family"


class EventCategory(Enum):
    MARKET = "market"
    LIFE = "life"
    CAREER = "career"
    EDUCATION = "education"


class Career(Enum):
    EMPLOYEE = "Employmee"
    ENTREPRENEUR = "Entrepreneur"
    UNEMPLOYED = "nemployed"
    STUDENT = "Student"


class PropertyCategory(Enum):
    HOUSE = "House"
    APPARTMENT = "Appartment"
    COTTAGE = "Cottage"
    CAR = "car"


class Property:
    name: str
    price: float
    category: PropertyCategory


@dataclass
class EventOption:
    description: str
    execute: Callable[[Player], Any]
    requirements: Optional[Callable[[Player], bool]] = None


@dataclass
class Event:
    title: str
    description: str
    options: List[EventOption]
    category: str  # life, market, career, education

    def get_available_options(self, player: Player) -> List[EventOption]:
        return [
            opt
            for opt in self.options
            if not opt.requirements or opt.requirements(player)
        ]


# TODO: fix mockup life events
def create_life_events() -> List[Event]:
    events = [
        Event(
            "Marriage Proposal",
            "You're considering getting married. This will affect your finances and life decisions.",
            [
                EventOption(
                    "Get married (Cost: $20,000)",
                    lambda player: (
                        player.spend_money(20000, "wedding"),
                        setattr(player, "is_married", True),
                        setattr(player, "happiness", min(100, player.happiness + 20)),
                    ),
                    lambda player: player.cash >= 20000
                    and not getattr(player, "is_married", False),
                ),
                EventOption("Stay single", lambda player: None),
            ],
            EventCategory.LIFE,
        ),
        Event(
            "Real Estate Investment",
            "You have an opportunity to invest in real estate.",
            [
                EventOption(
                    "Buy a house ($300,000, 20% down)",
                    lambda player: (
                        player.buy_a_property(300000, 0.2),
                        setattr(player, "happiness", min(100, player.happiness + 10)),
                    ),
                    lambda player: player.cash >= 60000,
                ),
                EventOption("Continue renting", lambda player: None),
            ],
            EventCategory.MARKET,
        ),
        Event(
            "Career Development",
            "An opportunity for career advancement has appeared!",
            [
                EventOption(
                    "Take advanced certification course (-$5,000)",
                    lambda player: (
                        player.spend_money(5000, "education"),
                        player.change_job(1.4),
                        setattr(player, "education", min(100, player.education + 15)),
                    ),
                    lambda player: player.cash >= 5000,
                ),
                EventOption("Stay in current position", lambda player: None),
            ],
            EventCategory.CAREER,
        ),
        Event(
            "Market Crash",
            "The stock market has crashed! Your investments are affected.",
            [
                EventOption(
                    "Sell everything", lambda player: player.sell_all_investments()
                ),
                EventOption(
                    "Buy the dip (-$10,000)",
                    lambda player: (player.invest(10000)),
                    lambda player: player.cash >= 10000,
                ),
                EventOption("Hold and wait", lambda player: None),
            ],
            EventCategory.MARKET,
        ),
        Event(
            "Job loss",
            "You were fired.",
            [
                EventOption(
                    "Apply for a new job, earning will be increased by 10%. You need to get a new certificate for 1000usd.",
                    lambda player: (
                        player.change_job(1.1),
                        player.spend_money(300, SpendingCategory.CERTIFICATION),
                        setattr(player, "happiness", max(0, player.happiness - 25)),
                    ),
                    lambda player: (player.cash > 300),
                ),
                EventOption(
                    "Be unemployed",
                    lambda player: (
                        player.change_job(0.4),
                        setattr(player, "happiness", max(0, player.happiness - 60)),
                    ),
                    lambda player: (player.monthly_income > 0),
                ),
            ],
            EventCategory.CAREER,
        ),
        Event(
            "Job loss",
            "You were fired.",
            [
                EventOption(
                    "Apply for a new job, earning will be increased by 10%. You need to get a new certificate for 1000usd.",
                    lambda player: (
                        player.change_job(1.1),
                        player.spend_money(300, SpendingCategory.CERTIFICATION),
                        setattr(player, "happiness", max(0, player.happiness - 25)),
                    ),
                    lambda player: (player.cash > 300),
                ),
                EventOption(
                    "Be unemployed",
                    lambda player: (
                        player.change_job(0.4),
                        setattr(player, "happiness", max(0, player.happiness - 60)),
                    ),
                    lambda player: (player.monthly_income > 0),
                ),
            ],
            EventCategory.CAREER,
        ),
        Event(
            "Buy a house",
            "You need to spend 5000000 CZK.",
            [
                EventOption(
                    "Buy a new house. Spending 5000000 CZK",
                    lambda player: (
                        player.buy_a_property(
                            Property(
                                name="family house",
                                price=5000000,
                                category=PropertyCategory.HOUSE,
                            )
                        ),
                        player.spend_money(5000000, SpendingCategory.PROPERTY_PURCHASE),
                        setattr(player, "happiness", min(100, player.happiness + 25)),
                    ),
                    lambda player: (player.cash > 5000000),
                ),
                EventOption("Do not buy any house", lambda player: None),
            ],
            EventCategory.LIFE,
        ),
        Event(
            "Buy a Car",
            "You need to spend 500000 CZK.",
            [
                EventOption(
                    "Buy a new car. Spending 500000 CZK",
                    lambda player: (
                        player.buy_a_property(
                            Property(
                                name="family car",
                                price=500000,
                                category=PropertyCategory.CAR,
                            )
                        ),
                        player.spend_money(500000, SpendingCategory.PROPERTY_PURCHASE),
                        setattr(player, "happiness", min(100, player.happiness + 15)),
                    ),
                    lambda player: (player.cash > 500000),
                ),
                EventOption("Do not buy any car", lambda player: None),
            ],
            EventCategory.LIFE,
        ),
        Event(
            "Have a child",
            "Your wife is pregnant, your child will be born in 7 months.",
            [
                EventOption(
                    "Accept new family situation.",
                    lambda player: (
                        player.spend_money(10000, SpendingCategory.FAMILY),
                        player.child_born,
                    ),
                    None,
                ),
                EventOption("Poor Man, there is no other option!", lambda player: None),
            ],
            EventCategory.LIFE,
        ),
    ]
    return events
