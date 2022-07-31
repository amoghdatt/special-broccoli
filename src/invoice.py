class Invoice:

    def __init__(self, item_details, total_sales_tax = 0, total = 0) -> None:
        self.item_details = item_details
        self.total_sales_tax = total_sales_tax
        self.total = total

    def print(self):
        for item_detail in self.item_details:
            cart_item  = item_detail[0]
            value_with_tax = item_detail[1]
            
            if cart_item.item.is_imported:
                print(f"{cart_item.quantity} {cart_item.item.is_imported} {cart_item.item.name}: {value_with_tax:.2f}")
            else:
                print(f"{cart_item.quantity} {cart_item.item.name}: {value_with_tax:.2f}")

        print(f"Sales Taxes: {self.total_sales_tax:.2f}\nTotal: {self.total:.2f}",end="")

    def add_item_details(self, item):
        self.item_details.append(item)

    def add_to_sales_tax(self, sales_tax):
        self.total_sales_tax += sales_tax

    def add_to_total(self, amount):
        self.total += amount
