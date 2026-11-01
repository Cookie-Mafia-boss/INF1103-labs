import json

#abstract class import
from abc import ABC, abstractmethod
#parent class
class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

   
    def to_dict(self):
        """Convert the Product object into a dictionary for JSON saving."""
        return {
            "TYPE": "base",
            "ID": self.product_id,
            "NAME": self.name,
            "PRICE": self.price,
            "STOCK": self.stock
        }

    #create display_information method to handle common attributes
    #Every child class must write their own version of this method!"
    @abstractmethod
    def display_information(self):
        
        print(f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price} | Stock: {self.stock}")
        
    @abstractmethod
    def get_fulfillment_info(self):
        pass
        
    def __str__(self):
        return f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price} | Stock: {self.stock}"

class CanbeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
    #The method should specify that implementing classes must provide a way to calculate shipping costs.
        pass


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

        # 1. Ask the user to choose the product type
        print("\nSelect Product Type:")
        print("1. Physical Product")
        print("2. Digital Product")
        choice = input("Enter choice (1 or 2): ").strip()

        # 2. Branch based on choice and instantiate the correct subclass
        if choice == "1":
            weight = input("Weight (e.g., 50g): ").strip()
            new_prod = PhysicalProduct(product_id, product_name, product_price, product_quantity, weight)
            
        elif choice == "2":
            download_size = input("Download Size (e.g., 70GB): ").strip()
            new_prod = DigitalProduct(product_id, product_name, product_price, product_quantity, download_size)
            
        else:
            print("Invalid choice. Product not added.")
            return

        # 3. Save it to inventory
        self.products.append(new_prod)
        self.save_inventory()
        print("Product added Successfully!")
    
    def display_inventory(self):
        print("1. Display all products")
        if not self.products:
            print("No products currently in list.")
        else:
            for item in self.products:
                item.display_information()
                if isinstance(item, CanbeShipped):
                    cost = item.calculate_shipping_cost()
                    print(f"Shipping Cost: ${cost:.2f}")
                print("-" * 40)
        print("\n")

    def update_stock(self):
        #3. Update Stock        
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
        #4. Search Product      
        search_id = input("Enter Product ID to search: ").strip()
        found = False
        for product in self.products:
            if product.product_id == search_id:
                print(f"\nProduct Found:")
                product.display_information()
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
                
                self.products = []
                for item in data:
                    prod_type = item.get("TYPE")
                    if prod_type == "physical":
                        prod = PhysicalProduct(
                            item["ID"], item["NAME"], item["PRICE"], item["STOCK"], item.get("WEIGHT", "0g")
                        )
                        self.products.append(prod)
                    elif prod_type == "digital":
                        prod = DigitalProduct(
                            item["ID"], item["NAME"], item["PRICE"], item["STOCK"], item.get("DOWNLOAD_SIZE", "0GB")
                        )
                        self.products.append(prod)
                    else:
                        # Fallback for old data files without TYPE key
                        prod = PhysicalProduct(
                            item["ID"], item["NAME"], item["PRICE"], item["STOCK"], "0g"
                        )
                        self.products.append(prod)
        except FileNotFoundError:
            pass # File doesn't exist yet, start empty

#child class from Product
class PhysicalProduct(Product, CanbeShipped):
    def __init__(self,product_id, name, price, stock,weight):

        #use super() function to extract the parents's attributes
        super().__init__(product_id,name,price,stock)
        self.weight = weight

    def display_information(self):
        # 1. Runs the parent's method first (prints ID, name, price, stock)
            super().display_information()
            
        # 2. Adds the unique child attribute
            print(f"Weight: {self.weight}")
            self.get_fulfillment_info()

    def get_fulfillment_info(self):
            print("product requires physical shipping as it is a physical product.")

    def calculate_shipping_cost(self):
        #shipping cost logic (standard rate of 2.50 shipping fee , if product exceed 500g charge another dollar)
       # convert str to int
        cleaned_weight = self.weight.lower().replace("g", "").strip()
        try:
            weight_value = float(cleaned_weight)
        except ValueError:
            weight_value = 0.0
        
        # Set the base rate
        shipping_cost = 2.50
        
        # Check if it exceeds 500g
        if weight_value > 500:
            shipping_cost += 1.00  # Add an extra dollar
            print(f"Weight ({self.weight}) exceeds 500g. Added $1.00 extra fee.")
        else:
            print(f"Weight ({self.weight}) is 500g or under. Standard rate applies.")
            
        return shipping_cost

    def to_dict(self):
        data = super().to_dict()
        data["TYPE"] = "physical"
        data["WEIGHT"] = self.weight
        return data

#Testing the functionality

#physicalproduct = PhysicalProduct("14000", "PokemonZA" , "89.99", "50", "50g")
#print(physicalproduct.product_id)
#print(physicalproduct.weight)

#child class form PhysicalProduct
class DigitalProduct(Product):
    def __init__(self,product_id,name,price,stock,download_size):

        #use super function to extract from the parent class
        super().__init__(product_id,name,price,stock)
        self.download_size = download_size

    def display_information(self):
        # 1. Runs the parent's method first (prints ID, name, price, stock)
        super().display_information()

        # 2. Adds the unique child attribute
        print(f"Download Size: {self.download_size}")
        self.get_fulfillment_info()

    def get_fulfillment_info(self):
        print("Delivered instantly through an online download link.")

    def to_dict(self):
        data = super().to_dict()
        data["TYPE"] = "digital"
        data["DOWNLOAD_SIZE"] = self.download_size
        return data

#test digital product class
#digitalproduct = DigitalProduct("15000", "ZELDA TOTK", "99.99", "50", "70gb")
#print(digitalproduct.price)
#print(digitalproduct.download_size)

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