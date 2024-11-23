from typing import List, Optional
import random
from src.app.events import Event, EventOption
from src.app.player import Player


class GameEngine:
    def __init__(self):
        self.current_month = 0
        self.events = self._initialize_events()

    def _initialize_events(self) -> List[Event]:
        events = [
            Event(
                "Job Opportunity",
                "A new job opportunity has appeared!",
                [
                    EventOption(
                        "Accept new job",
                        lambda player: player.change_job(salary_increase=1.2),
                    ),
                    EventOption("Stay at current job", lambda player: None),
                ],
            ),
            Event(
                "Investment Opportunity",
                "Stock market is showing promising signs!",
                [
                    EventOption(
                        "Invest in stocks",
                        lambda player: player.invest(player.cash * 0.3),
                    ),
                    EventOption("Skip this opportunity", lambda player: None),
                ],
            ),
            Event(
                "Education Opportunity",
                "You can take a professional course to improve your skills!",
                [
                    EventOption(
                        "Take the course (-$1000)",
                        lambda player: player.spend_money(1000, "education"),
                    ),
                    EventOption("Skip the course", lambda player: None),
                ],
            ),
        ]
        return events

    def get_current_event(self) -> Optional[Event]:
        if random.random() < 0.3:  # 30% chance of event
            return random.choice(self.events)
        return None

    def advance_month(self):
        self.current_month += 1
