from model import Booking
from service import BookingService


class BookingApplication:
    def run(self):
        booking = Booking(
            reference="BK-204",
            guest_name="Grace Hopper",
            guest_email="grace@example.org",
            room_type="sea_view",
            nights=3,
            breakfast=True,
        )
        total = BookingService().confirm(booking)
        print(f"Stored booking total: EUR {total:.2f}")
