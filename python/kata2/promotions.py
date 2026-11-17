class PromotionBanner:
    def text(self, cart):
        if cart.subtotal >= 50 and cart.country == "ES":
            return "Free shipping unlocked"
        if cart.country == "ES":
            return f"Spend EUR {50 - cart.subtotal:.2f} more for free shipping"
        return "International shipping applies"
