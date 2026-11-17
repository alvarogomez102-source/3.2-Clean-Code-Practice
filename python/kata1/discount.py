class DiscountRules:
    def amount(self, sale, subtotal):
        if sale.member:
            if subtotal >= 20:
                return round(subtotal * 0.10, 2)
        return 0
