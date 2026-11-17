class EmailConfirmationSender:
    def send(self, attendee, amount):
        print(f"EMAIL to {attendee.email}: registration confirmed, EUR {amount:.2f}")
