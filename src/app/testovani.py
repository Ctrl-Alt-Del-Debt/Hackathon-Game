from events import Event
from player import Player, Career
from events import Event, EventCategory, EventOption

test_player = Player(name="Pepa", age=34, career = Career.EMPLOYEE)

test_event = Event(
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
    )

test_event.options[0].execute

if test_player.is_married is False:
    print("Player got married")
else:
    raise Exception("There is a problem. ")