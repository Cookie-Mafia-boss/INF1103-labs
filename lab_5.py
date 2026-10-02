def inventory_dic():
    this_inventory = {
        "ID" : "Lenovo Yoga",
        "NAME" : "Airpods Max",
        "PRICE" : "Logitech G50",
        "STOCK" : "Razer Keyboard"
    }

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

def 

#Main Loop
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
        print(inventory_dic())
        print("\n")
        print("\n")

    elif user_selection == "2":
        print("2. Add Product         ")
        new_inventory = create_inventory()
        

    elif user_selection == "3":
         print("3. Update Stock        ")

    elif user_selection == "4":
        print("4. Search Product      ")

    elif user_selection == "5":
        print("5. Save Inventory      ")

    elif user_selection == "6":
        print("6. Exit                ")
        print("Saving inventory before exit...")
        print("Inventory saved successfully")
        print("\n")

        print("Thank you for using Inventory Management System.")
        print("Program terminated")
        break
    else: 
        print("Invalid selection, pls enter a valid selection")

