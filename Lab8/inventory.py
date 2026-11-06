# inventory.py
import json
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class Inventory:
    def __init__(self, filename: str = "inventory.json"):
        self.filename: str = filename
        self.products: list[Product] = []  # Managed collection using the base Product class type
        self.load_inventory() 

    def add_product(self, product: Product) -> None:
        """Add an existing Product object to the inventory."""
        self.products.append(product)
        self.save_inventory()
        print(f"Added product '{product.name}' to inventory.")

    def remove_product(self, product_id: str) -> None:
        """Remove the matching Product reference from the inventory."""
        product_to_remove = self.find_product(product_id)
        if product_to_remove:
            self.products.remove(product_to_remove)
            self.save_inventory()
            print(f"Removed product ID {product_id} from inventory.")
        else:
            print(f"Product ID {product_id} not found in inventory.")

    def find_product(self, product_id: str) -> Product | None:
        """Return the matching Product, or None if it cannot be found."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        """Polymorphic display method that works purely with the Product abstraction (LSP)."""
        print("\n=== Current Inventory Status ===")
        if not self.products:
            print("No products currently in list.")
        else:
            for product in self.products:
                product.display_information()
                print(f"  > Fulfillment: {product.get_fulfillment_info()}")
                print("-" * 50)
        print("\n")

    def update_stock(self) -> None:
        stock_input = input("Enter Product ID: ").strip()
        product = self.find_product(stock_input)

        if product:
            print(f"\nProduct Found: {product.name} (Current Stock: {product.stock})")
            try:
                change = int(input("Enter stock change (positive to add, negative to reduce): "))
                if product.stock + change < 0:
                    print("Error: Stock cannot become negative.")
                    return
                product.update_stock(change)
                self.save_inventory()
                print(f"Stock updated successfully. New quantity: {product.stock}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            return
        print("Product ID not found.")

    def save_inventory(self) -> None:
        data = []
        for prod in self.products:
            prod_dict = prod.to_dict()
            if isinstance(prod, PhysicalProduct):
                prod_dict["TYPE"] = "physical"
                prod_dict["WEIGHT"] = prod.weight
            elif isinstance(prod, DigitalProduct):
                prod_dict["TYPE"] = "digital"
                prod_dict["DOWNLOAD_SIZE"] = prod.file_size
            data.append(prod_dict)

        with open(self.filename, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load_inventory(self) -> None:
        try:
            with open(self.filename, "r") as json_file:
                data = json.load(json_file)
                if isinstance(data, dict):
                    data = [data]
                
                self.products = []
                for item in data:
                    prod_type = item.get("TYPE")
                    sup_data = item.get("SUPPLIER", {})
                    supplier_obj = Supplier(
                        sup_data.get("SUPPLIER_ID", "Unknown"),
                        sup_data.get("SUPPLIER_NAME", "Unknown"),
                        sup_data.get("CONTACT_EMAIL", "Unknown")
                    )

                    if prod_type == "physical":
                        prod = PhysicalProduct(
                            item["ID"], item["NAME"], item["PRICE"], item["STOCK"], supplier_obj, item.get("WEIGHT", "0kg")
                        )
                        self.products.append(prod)
                    elif prod_type == "digital":
                        prod = DigitalProduct(
                            item["ID"], item["NAME"], item["PRICE"], item["STOCK"], supplier_obj, item.get("DOWNLOAD_SIZE", "0GB")
                        )
                        self.products.append(prod)
        except FileNotFoundError:
            pass