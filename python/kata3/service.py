from delivery import ConsoleConfirmationSender
from rates import RoomRateTable
from storage import CsvBookingStore
from validation import BookingValidator

BREAKFAST_RATE = 12

class BookingService:
    def __init__(self):
        self.validator = BookingValidator()
        self.rates = RoomRateTable()
        self.store = CsvBookingStore()
        self.sender = ConsoleConfirmationSender()

    def confirm(self, booking):
        self.validator.validate(booking)
        total = self.calc_total(booking)
        self.store.save(booking, total)
        self.sender.send(booking, total)
        return total

    def calc_total(self, booking):
        self.validator.validate(booking)
        total = self.rates.rate_for(booking.room_type) * booking.nights
        if booking.breakfast:
            total += booking.nights * BREAKFAST_RATE
        return total
