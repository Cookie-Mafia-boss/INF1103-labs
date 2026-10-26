import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        """Convert the Product object into a dictionary for JSON saving."""
        return {
            "ID": self.product_id,
            "NAME": self.name,
            "PRICE": self.price,
            "STOCK": self.stock
        }

    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price} | Stock: {self.stock}"


class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.products = []
        self.load_inventory() 

    def add_product(self):
        print("==================")
        print("Add new product ")
        print("==================")
        print("\n")

        product_id = input("Product Id    : ").strip()
        product_name = input("Product Name  : ").strip()
        try:
            product_price = float(input("Price         : "))
            product_quantity = int(input("Stock Quantity: "))
        except ValueError:
            print("Invalid price or stock quantity. Product not added.")
            return

        # Create a Product instance
        new_prod = Product(product_id, product_name, product_price, product_quantity)
        self.products.append(new_prod)
        self.save_inventory()
        print("Product added Successfully")

    def display_inventory(self):
        print("1. Display all products")
        if not self.products:
            print("No products currently in list.")
        else:
            for item in self.products:
                print(item)
        print("\n")

    def update_stock(self):
        print("3. Update Stock        ")
        stock_input = input("Enter Product ID: ").strip()

        for product in self.products:
            if product.product_id == stock_input:
                print(f"\nProduct Found:")
                print(f"Name: {product.name}")
                print(f"Current Stock: {product.stock}\n")

                try:
                    new_quantity = int(input("New Stock Quantity: "))
                    if new_quantity < 0:
                        print("Stock cannot be negative.")
                        return
                    
                    product.stock = new_quantity
                    self.save_inventory()
                    print(f"Stock for '{product.name}' updated to {new_quantity}.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                return

        print("Product ID not found.")

    def search_product(self):
        print("4. Search Product      ")
        search_id = input("Enter Product ID to search: ").strip()
        found = False
        for product in self.products:
            if product.product_id == search_id:
                print(f"\nProduct Found:")
                print(product)
                found = True
                break
        if not found:
            print("Product ID not found.")

    def save_inventory(self):
        # Convert list of Product objects to a list of dictionaries for JSON
        data = [prod.to_dict() for prod in self.products]
        with open(self.filename, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def load_inventory(self):
        try:
            with open(self.filename, "r") as json_file:
                data = json.load(json_file)
                # Handle single dictionary or list format from earlier files
                if isinstance(data, dict):
                    data = [data]
                for item in data:
                    prod = Product(item["ID"], item["NAME"], item["PRICE"], item["STOCK"])
                    self.products.append(prod)
        except FileNotFoundError:
            pass # File doesn't exist yet, start empty


# --- Main Loop ---
my_inventory = Inventory()

while True:
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================")
    print("\n\n")

    print("--------Menu------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-------------------------")
    
    user_selection = input("please Enter your selection  :")
    print("\n")

    if user_selection == "1":
        my_inventory.display_inventory()
    elif user_selection == "2":
        my_inventory.add_product()
    elif user_selection == "3":
        my_inventory.update_stock()
    elif user_selection == "4":
        my_inventory.search_product()
    elif user_selection == "5":
        print("5. Save Inventory      ")
        my_inventory.save_inventory()
        print("Inventory saved successfully")
    elif user_selection == "6":
        print("6. Exit                ")
        print("Saving inventory before exit...")
        my_inventory.save_inventory()
        print("Inventory saved successfully\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated")
        break
    else: 
        print("Invalid selection, pls enter a valid selection")