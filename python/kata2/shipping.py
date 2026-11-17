class ShippingCalculator:
    def cost(self, cart):
        if cart.country == "ES" and cart.subtotal >= 50:
            return 0
        if cart.country == "ES":
            return 5
        return 15
