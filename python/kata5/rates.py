class TicketRates:
    def base_for(self, ticket_type):
        rates = {
            "standard": 120,
            "student": 80,
            "sponsor": 250
        }
        if ticket_type in rates:
            return rates[ticket_type]
        raise ValueError("Unknown ticket type")
