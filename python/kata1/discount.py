class DiscountRules:
    def amount(self, sale, subtotal):
        if (not sale.member or
            subtotal < 20):
            return 0
        return round(subtotal * 0.10, 2)
