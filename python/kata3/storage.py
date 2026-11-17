import csv
from pathlib import Path


class CsvBookingStore:
    def save(self, booking, total):
        path = Path("bookings.csv")
        new_file = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if new_file:
                writer.writerow(["reference", "guest", "room", "nights", "total"])
            writer.writerow(
                [booking.reference, booking.guest_name, booking.room_type, booking.nights, total]
            )
