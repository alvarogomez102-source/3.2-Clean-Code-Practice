class ConsoleConfirmationSender:
    def send(self, booking, total):
        print(
            f"EMAIL to {booking.guest_email}: "
            f"Booking {booking.reference} confirmed for EUR {total:.2f}"
        )
