from dataclasses import dataclass
from typing import List, Callable
from src.app.player import Player


@dataclass
class EventOption:
    description: str
    execute: Callable[[Player], None]


@dataclass
class Event:
    title: str
    description: str
    options: List[EventOption]
