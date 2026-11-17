import csv
from pathlib import Path


class CsvRegistrationStore:
    def save(self, conference, attendee, amount):
        path = Path("registrations.csv")
        new_file = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if new_file:
                writer.writerow(["conference", "name", "email", "ticket", "group", "total"])
            writer.writerow(
                [conference.code, attendee.name, attendee.email, attendee.ticket_type,
                 attendee.group_size, amount]
            )
