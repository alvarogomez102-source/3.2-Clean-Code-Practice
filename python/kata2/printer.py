class QuotePrinter:
    def print_quote(self, quote, banner):
        print(f"Subtotal: EUR {quote.subtotal:.2f}")
        print(f"Shipping: EUR {quote.shipping:.2f}")
        print(f"Total: EUR {quote.total:.2f}")
        print(banner)
