# product.py
from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.product_id: str = product_id
        self.name: str = name
        self.price: float = price
        self.stock: int = stock
        self.supplier: Supplier = supplier  # Aggregation: Product has a Supplier object

    @abstractmethod
    def display_information(self) -> None:
        """Displays details about this product."""
        pass

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        """Returns delivery/fulfillment instructions."""
        pass
    
    def _display_common_info(self) -> None:
        """Helper to display common attributes for all products uniformly (LSP compliant)."""
        print(f"[{type(self).__name__}] ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}")
        if self.supplier:
            print(f"  Supplier: {self.supplier.supplier_name} ({self.supplier.contact_email})")

    def update_stock(self, quantity: int) -> None:
        """Update the product's stock count."""
        self.stock += quantity

    def to_dict(self) -> dict:
        """Convert the Product object into a dictionary for JSON saving."""
        return {
            "ID": self.product_id,
            "NAME": self.name,
            "PRICE": self.price,
            "STOCK": self.stock,
            "SUPPLIER": {
                "SUPPLIER_ID": self.supplier.supplier_id,
                "SUPPLIER_NAME": self.supplier.supplier_name,
                "CONTACT_EMAIL": self.supplier.contact_email
            }
        }
        
    def __str__(self) -> str:
        return f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock} | Supplier: {self.supplier.supplier_name}"

class CanBeShipped(ABC):
    """Mix-in interface for shippable products."""
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass