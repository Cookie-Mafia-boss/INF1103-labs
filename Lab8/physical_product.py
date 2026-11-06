# physical_product.py
from product import Product, CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: str):
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: str = weight

    def display_information(self) -> None:
        """Polymorphic display implementation for physical items."""
        super()._display_common_info()
        print(f"  Weight: {self.weight}")
        print(f"  Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfillment_info(self) -> str:
        return f"Ships via courier service. Package weight: {self.weight}"

    def calculate_shipping_cost(self) -> float:
        return 15.00  # Flat or weight-calculated shipping rule