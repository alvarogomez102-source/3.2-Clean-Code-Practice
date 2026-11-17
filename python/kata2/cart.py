from promotions import PromotionBanner
from quote import ShippingQuote
from shipping import ShippingCalculator
from printer import QuotePrinter


class Cart:
    def __init__(self, country):
        self.country = country
        self.items = []
        self.subtotal = None

    def load(self, items):
        self.items = list(items)

    def calculate(self):
        self.subtotal = round(
            sum(item.price * item.quantity for item in self.items), 2
        )

    def shipping(self):
        if self.subtotal is None:
            raise RuntimeError("Call calculate() before shipping()")
        return ShippingCalculator().cost(self)

    def banner(self):
        if self.subtotal is None:
            raise RuntimeError("Call calculate() before banner()")
        return PromotionBanner().text(self)

    def print_quote(self):
        if self.subtotal is None:
            raise RuntimeError("Call calculate() before print_quote()")
        quote = ShippingQuote(self.subtotal, self.shipping(), self.subtotal + self.shipping())
        QuotePrinter().print_quote(quote, self.banner())
