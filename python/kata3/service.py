from delivery import ConsoleConfirmationSender
from rates import RoomRateTable
from storage import CsvBookingStore
from validation import BookingValidator


class BookingService:
    def __init__(self):
        self.validator = BookingValidator()
        self.rates = RoomRateTable()
        self.store = CsvBookingStore()
        self.sender = ConsoleConfirmationSender()

    def confirm(self, booking):
        self.validator.validate(booking)
        total = self.rates.rate_for(booking.room_type) * booking.nights
        if booking.breakfast:
            total += booking.nights * 12
        self.store.save(booking, total)
        self.sender.send(booking, total)
        return total
