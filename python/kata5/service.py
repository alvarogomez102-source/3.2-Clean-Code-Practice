from dashboard import RegistrationDashboard
from delivery import EmailConfirmationSender
from rates import TicketRates
from storage import CsvRegistrationStore


class RegistrationService:
    def __init__(self, conference):
        self.conference = conference
        self.pending = None
        self.receipts = []
        self.audit = []
        self.rates = TicketRates()
        self.store = CsvRegistrationStore()
        self.sender = EmailConfirmationSender()
        self.report = RegistrationDashboard()

    def prepare(self, attendee):
        if not attendee.name or "@" not in attendee.email:
            raise ValueError("Name and email are required")
        if attendee.group_size < 1:
            raise ValueError("Group size must be positive")
        self.pending = attendee

    def quote(self):
        if self.pending is None:
            raise RuntimeError("Call prepare() before quote()")
        a = self.pending
        base = self.rates.base_for(a.ticket_type)
        subtotal = base * a.group_size
        if self.conference.days_until_event >= 30:
            subtotal *= 0.85
        if a.group_size >= 3:
            subtotal *= 0.90
        if a.wants_meal:
            subtotal += 20 * a.group_size
        total = round((subtotal + 5) * 1.07, 2)
        self.audit.append(f"QUOTED {a.email} EUR {total:.2f}")
        return total

    def register(self):
        if self.pending is None:
            raise RuntimeError("Call prepare() before register()")
        a = self.pending
        amount = self.quote()
        self.store.save(self.conference, a, amount)
        self.receipts.append((a, amount))
        self.sender.send(a, amount)
        self.pending = None
        return amount

    def dashboard(self):
        return self.report.build(self.conference, self.receipts, self.audit)
