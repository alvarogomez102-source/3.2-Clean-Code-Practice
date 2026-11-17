from dataclasses import dataclass


@dataclass
class Booking:
    reference: str
    guest_name: str
    guest_email: str
    room_type: str
    nights: int
    breakfast: bool
