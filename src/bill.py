class Bill:

    def __init__(self, bill_details, total_sales_tax, total) -> None:
        self.bill_details = bill_details
        self.total_sales_tax = total_sales_tax
        self.total = total

    def print(self):
        for bill_item in self.bill_details:
            cart_item  = bill_item[0]
            value_with_tax = bill_item[1]
            print(f"{cart_item.quantity} {cart_item.item.name}: {value_with_tax:.2f}")

        print(f"Sales Taxes: {self.total_sales_tax:.2f}\nTotal: {self.total:.2f}",end="")
