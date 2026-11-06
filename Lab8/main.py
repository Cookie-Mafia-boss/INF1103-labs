from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def main():
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
        
        user_selection = input("Please enter your selection: ")
        print("\n")

        if user_selection == "1":
            # Updated to match the polymorphic display method name
            my_inventory.display_all_products()
            
        elif user_selection == "2":
            print("==================")
            print("Add new product ")
            print("==================")
            
            # 1. Gather Supplier details first (Aggregation requirement)
            print("\n--- Supplier Information ---")
            sup_id = input("Supplier ID   : ").strip()
            sup_name = input("Supplier Name : ").strip()
            sup_email = input("Contact Email : ").strip()
            supplier_obj = Supplier(sup_id, sup_name, sup_email)

            # 2. Gather Product details
            print("\n--- Product Information ---")
            product_id = input("Product ID    : ").strip()
            product_name = input("Product Name  : ").strip()
            
            try:
                product_price = float(input("Price         : "))
                product_quantity = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid price or stock quantity. Product not added.\n")
                continue

            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == "1":
                weight = input("Weight (e.g., 2.5kg): ").strip()
                new_prod = PhysicalProduct(product_id, product_name, product_price, product_quantity, supplier_obj, weight)
            elif choice == "2":
                download_size = input("Download Size (e.g., 500MB): ").strip()
                new_prod = DigitalProduct(product_id, product_name, product_price, product_quantity, supplier_obj, download_size)
            else:
                print("Invalid choice. Product not added.\n")
                continue

            # 3. Pass the created Product object into Inventory (Aggregation)
            my_inventory.add_product(new_prod)
            print("Product added successfully!\n")

        elif user_selection == "3":
            my_inventory.update_stock()
            
        elif user_selection == "4":
            my_inventory.search_product()
            
        elif user_selection == "5":
            print("5. Save Inventory")
            my_inventory.save_inventory()
            print("Inventory saved successfully\n")
            
        elif user_selection == "6":
            print("6. Exit")
            print("Saving inventory before exit...")
            my_inventory.save_inventory()
            print("Inventory saved successfully\n")
            print("Thank you for using Inventory Management System.")
            print("Program terminated")
            break
            
        else: 
            print("Invalid selection, please enter a valid selection\n")

if __name__ == "__main__":
    main()