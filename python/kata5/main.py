from models import Attendee, Conference
from service import RegistrationService


def main():
    conference = Conference("SE-27", "Software Engineering Day", 45)
    service = RegistrationService(conference)
    attendees = [
        Attendee("Alan Turing", "alan@example.org", "standard", 1, True),
        Attendee("Margaret Hamilton", "margaret@example.org", "student", 3, False),
    ]
    for attendee in attendees:
        service.prepare(attendee)
        print(f"Quote for {attendee.name}: EUR {service.quote():.2f}")
        service.register()
    print("Dashboard:", service.dashboard())


if __name__ == "__main__":
    main()
