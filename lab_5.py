import json

def inventory_dic():
    this_inventory = {
        "ID" : "5000",
        "NAME" : "Airpods Max",
        "PRICE" : "50.67",
        "STOCK" : "50"
    }

    with open("inventory.json", "w") as json_file:
        json.dump(this_inventory, json_file, indent=4)

    return(this_inventory)

def create_inventory():
    print("==================")
    print("Add new product ")
    print("==================")
    print("\n")

    # 1. Collect inputs first
    product_id = input("Product Id    : ")
    product_name = input("Product Name  : ")
    product_price = float(input("Price         : "))
    product_quantity = int(input("Stock Quantity: "))

    # 2. Assign values to dictionary keys
    new_product = {
        "ID": product_id,
        "NAME": product_name,
        "PRICE": product_price,
        "STOCK": product_quantity
    }

    return(new_product)

# Initialize master inventory list
list_inventory = []

def update_stock(inventory):
    stock_input = input("Enter Product ID: ").strip()

    # Iterate through each product dictionary in the inventory list
    for product in inventory:
        # Check if the current product's ID matches user input
        if product["ID"] == stock_input:
            print(f"\nProduct Found:")
            print(f"Name: {product['NAME']}")
            print(f"Current Stock: {product['STOCK']}\n")

            try:
                new_quantity = int(input("New Stock Quantity: "))
                if new_quantity < 0:
                    print("Stock cannot be negative.")
                    return
                
                # Update the stock value in the dictionary
                product["STOCK"] = new_quantity
                print(f"Stock for '{product['NAME']}' updated to {new_quantity}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            
            return  # Stop searching once the product is found and updated

    # If the loop finishes without returning, the ID wasn't in the list
    print("Product ID not found.")

def save_inventory(data):
    with open("inventory.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

# Main Loop
while True:
    print("=========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=========================================")
    
    print("\n")
    print("\n")

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
        print("1. Display all products")
        if not list_inventory:
            print("No products currently in list.")
        else:
            for item in list_inventory:
                print(item)
        print("\n")

    elif user_selection == "2":
        print("2. Add Product         ")
        new_inventory = create_inventory()
        list_inventory.append(new_inventory)
        save_inventory(list_inventory)  
        print("Product added Successfully")

    elif user_selection == "3":
        print("3. Update Stock        ")
        update_stock(list_inventory)

    elif user_selection == "4":
        print("4. Search Product      ")
        search_id = input("Enter Product ID to search: ").strip()
        found = False
        for product in list_inventory:
            if product["ID"] == search_id:
                print(f"\nProduct Found:")
                print(f"ID: {product['ID']} | Name: {product['NAME']} | Price: ${product['PRICE']} | Stock: {product['STOCK']}")
                found = True
                break
        if not found:
            print("Product ID not found.")

    elif user_selection == "5":
        print("5. Save Inventory      ")
        save_inventory(list_inventory)
        print("Inventory saved successfully")

    elif user_selection == "6":
        print("6. Exit                ")
        print("Saving inventory before exit...")
        save_inventory(list_inventory)
        print("Inventory saved successfully")
        print("\n")

        print("Thank you for using Inventory Management System.")
        print("Program terminated")
        break
    else: 
        print("Invalid selection, pls enter a valid selection")