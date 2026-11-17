from cart import Cart
from item import CartItem


class CartApplication:
    def run(self):
        cart = Cart("ES")
        cart.load(
            [
                CartItem("Notebook", 12.50, 2),
                CartItem("Headphones", 30.00, 1),
            ]
        )
        cart.calculate()
        cart.print_quote()
