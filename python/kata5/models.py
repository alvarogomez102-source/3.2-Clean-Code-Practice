from dataclasses import dataclass


@dataclass(frozen=True)
class Attendee:
    name: str
    email: str
    ticket_type: str
    group_size: int
    wants_meal: bool


@dataclass(frozen=True)
class Conference:
    code: str
    title: str
    days_until_event: int
