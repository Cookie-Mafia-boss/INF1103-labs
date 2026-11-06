class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        """Create and own an OrderLine internally, then add it to the order."""
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        """Calculate and return the total value of the order by summing all line subtotals."""
        return sum(line.calculate_subtotal() for line in self.order_lines)

    def display_order(self) -> None:
        """Display order details and line items."""
        print(f"Order ID: {self.order_id}")
        for line in self.order_lines:
            subtotal = line.calculate_subtotal()
            print(f"  - {line.quantity}x {line.product.name} @ ${line.product.price:.2f} each | Subtotal: ${subtotal:.2f}")
        print(f"Total Order Value: ${self.calculate_total():.2f}\n")