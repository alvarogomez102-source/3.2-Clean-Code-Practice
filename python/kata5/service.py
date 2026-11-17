from dashboard import RegistrationDashboard
from delivery import EmailConfirmationSender
from rates import TicketRates
from storage import CsvRegistrationStore

DAYS_UNTIL_EVENT_DISCOUNT_TIME = 30
DAYS_UNTIL_EVENT_DISCOUNT = 0.85
GROUP_SIZE_DISCOUNT = 0.9
MEAL_RATE = 20.0
TAX_RATE = 1.07
SERVICE_PRICE = 5.0

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
        if self.conference.days_until_event >= DAYS_UNTIL_EVENT_DISCOUNT_TIME:
            subtotal *= DAYS_UNTIL_EVENT_DISCOUNT
        if a.group_size >= 3:
            subtotal *= GROUP_SIZE_DISCOUNT
        if a.wants_meal:
            subtotal += MEAL_RATE * a.group_size
        total = round((subtotal + SERVICE_PRICE) * TAX_RATE, 2)
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
