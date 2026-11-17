from discount import DiscountRules


class PriceCalculator:
    def __init__(self):
        self.rules = DiscountRules()

    def calc(self, sale):
        total = self.calc_total(sale)
        discount = self.calc_discount(sale, total)
        return round(total - discount, 2), discount

    def calc_total(self, sale):
        return sum(item.price * item.quantity for item in sale.items)

    def calc_discount(self, sale, total):
        return self.rules.amount(sale, total)