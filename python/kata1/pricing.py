from discount import DiscountRules


class PriceCalculator:
    def __init__(self):
        self.rules = DiscountRules()

    def calc(self, sale):
        x = 0
        for item in sale.items:
            x += item.price * item.quantity
        discount = self.rules.amount(sale, x)
        if sale.member and x >= 20:
            print("Member discount applied")
        return round(x - discount, 2), discount
