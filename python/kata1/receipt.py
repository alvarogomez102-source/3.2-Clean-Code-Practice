class ReceiptPrinter:
    def print_receipt(self, sale, total, discount):
        if discount > 0:
            print("Member discount applied")
        print("Receipt for", sale.customer)
        for item in sale.items:
            print(f"{item.quantity} x {item.name}: EUR {item.price * item.quantity:.2f}")
        print(f"Discount: EUR {discount:.2f}")
        print(f"Total: EUR {total:.2f}")
