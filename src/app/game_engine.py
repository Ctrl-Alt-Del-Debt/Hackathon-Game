from typing import List, Optional
import random
from src.app.events import Event, EventOption, create_life_events
from src.app.player import Player


class GameEngine:
    def __init__(self):
        self.current_month = 0
        self.events = self._initialize_events()

    def _initialize_events(self) -> List[Event]:

        events = create_life_events()
        return events

    def _check_market_conditions(self) -> Optional[Event]:
        # Simulate market conditions
        market_event = None
        if random.random() < 0.1:  # 10% chance of market event
            if random.random() < 0.3:  # 30% chance of crash when market event occurs
                market_event = Event(
                    "Market Crash",
                    "The stock market has crashed! Your investments are at risk.",
                    [
                        EventOption(
                            "Sell everything",
                            lambda player: player.sell_all_investments(),
                        ),
                        EventOption("Hold positions", lambda player: None),
                        EventOption(
                            "Buy the dip",
                            lambda player: (player.invest(player.cash * 0.5), None)[-1],
                            lambda player: player.cash >= 5000,
                        ),
                    ],
                    "market",
                )
            else:
                market_event = Event(
                    "Bull Market",
                    "The market is showing strong growth potential!",
                    [
                        EventOption(
                            "Invest heavily",
                            lambda player: (player.invest(player.cash * 0.7), None)[-1],
                            lambda player: player.cash >= 1000,
                        ),
                        EventOption(
                            "Make small investment",
                            lambda player: (player.invest(player.cash * 0.3), None)[-1],
                            lambda player: player.cash >= 500,
                        ),
                        EventOption("Skip opportunity", lambda player: None),
                    ],
                    "market",
                )
        return market_event

    def get_current_event(self) -> Optional[Event]:
        if random.random() < 0.3:  # 30% chance of event
            return random.choice(self.events)
        return None

    def advance_month(self):
        self.current_month += 1
