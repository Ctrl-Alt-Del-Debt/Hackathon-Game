from dataclasses import dataclass
from typing import List, Callable, Optional
from src.app.player import Player
import random


@dataclass
class EventOption:
    description: str
    execute: Callable[[Player], None]
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
                        None,
                    )[-1],
                    lambda player: player.cash >= 20000
                    and not getattr(player, "is_married", False),
                ),
                EventOption("Stay single", lambda player: None),
            ],
            "life",
        ),
        Event(
            "Real Estate Investment",
            "You have an opportunity to invest in real estate.",
            [
                EventOption(
                    "Buy a house ($300,000, 20% down)",
                    lambda player: (
                        player.buy_property(300000, 0.2),
                        setattr(player, "happiness", min(100, player.happiness + 10)),
                        None,
                    )[-1],
                    lambda player: player.cash >= 60000,
                ),
                EventOption("Continue renting", lambda player: None),
            ],
            "market",
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
                        None,
                    )[-1],
                    lambda player: player.cash >= 5000,
                ),
                EventOption("Stay in current position", lambda player: None),
            ],
            "career",
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
                    lambda player: (player.invest(10000), None)[-1],
                    lambda player: player.cash >= 10000,
                ),
                EventOption("Hold and wait", lambda player: None),
            ],
            "market",
        ),
    ]
    return events
