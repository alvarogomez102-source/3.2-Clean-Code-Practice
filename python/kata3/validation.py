class BookingValidator:
    def validate(self, booking):
        if not booking.reference or booking.nights < 1:
            raise ValueError("Reference and a positive stay are required")
        if "@" not in booking.guest_email:
            raise ValueError("A guest email is required")
