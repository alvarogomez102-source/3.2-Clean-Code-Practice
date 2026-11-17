class RegistrationDashboard:
    def build(self, conference, receipts, audit):
        revenue = sum(amount for _, amount in receipts)
        group_bookings = sum(1 for attendee, _ in receipts if attendee.group_size >= 3)
        early_bookings = sum(1 for _ in receipts if conference.days_until_event >= 30)
        return {
            "registrations": len(receipts),
            "revenue": round(revenue, 2),
            "group_bookings": group_bookings,
            "early_bookings": early_bookings,
            "quotes_logged": len(audit),
        }
