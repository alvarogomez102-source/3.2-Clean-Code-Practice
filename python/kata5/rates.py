class TicketRates:
    def base_for(self, ticket_type):
        if ticket_type == "standard":
            return 120
        if ticket_type == "student":
            return 80
        if ticket_type == "sponsor":
            return 250
        raise ValueError("Unknown ticket type")
