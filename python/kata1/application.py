from models import CafeItem, Sale
from pricing import PriceCalculator
from receipt import ReceiptPrinter


class CafeApplication:
    def run(self):
        sale = Sale(
            "Ada",
            True,
            [
                CafeItem("Coffee", 3.50, 2),
                CafeItem("Sandwich", 8.00, 1),
                CafeItem("Cake", 4.50, 2),
            ],
        )
        total, discount = PriceCalculator().calc(sale)
        ReceiptPrinter().print_receipt(sale, total, discount)
