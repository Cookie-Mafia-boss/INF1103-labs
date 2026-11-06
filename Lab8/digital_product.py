# digital_product.py
from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, file_size: str):
        super().__init__(product_id, name, price, stock, supplier)
        self.file_size: str = file_size

    def display_information(self) -> None:
        """Polymorphic display implementation for digital items."""
        super()._display_common_info()
        print(f"  Download Size: {self.file_size}")

    def get_fulfillment_info(self) -> str:
        return f"Available via digital download link. File size: {self.file_size}"