print("=======================================================================")
print("Smart Inventory Auditor")
print("=======================================================================")

#Read file
def read_file():
    saved_data = "C:/SIT_INF1103/INF1103/Labs/Inventory.txt"

    try:
        #read saved inventory data
         with open(saved_data, 'r', encoding="utf8") as data:
            content = data.read()
            print("Existing inventory : ")
            print(content)

    except FileNotFoundError:
        print("No file as such exists")

        return(content)
# Input Validation
def get_valid_input():
    user_input = input("Enter Stock Quantity  :")
    
    if user_input == "":
        print("Please type something....")
        return None
    elif user_input.isdigit():
        return int(user_input)
    elif user_input == "quit" or user_input == "QUIT":
        return "quit"
    else:
        print("Invalid Input")
        return None

#Process Delivery Total
def process_delivery(current_total, new_value):
    return current_total + new_value

#Calculate 10% Tax
def calculate_tax(amount):
    return amount * 0.10

#Generate Report
def generate_report(total_units, failed_attempts, total_deliveries, total_tax):
    print("\n=======================================================================")
    print("Summary")
    print("=======================================================================")
    print(f"Total Units Processed             : {total_units}")
    print(f"Total Deliveries Processed        : {total_deliveries}")
    print(f"Total Tax (10%)                   : {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries : {failed_attempts}")
    print("=======================================================================")


# initialise values to 0 
inventory_init = 0
fail_reject = 0
inventory_pro_max = 0
deliveries_count = 0
total_tax = 0.0

read_file()

#Main loop
#continuous loop asking user to enter a stock quantity, until the user types quit
while True:
    validated_input = get_valid_input()

    if validated_input == "quit":
        print("Successfully exited the programme")
        break

    
    elif validated_input is None:
        fail_reject += 1

    else:
        
        integer = validated_input
        
        inventory_init = process_delivery(inventory_init, integer)
        tax_amount = calculate_tax(integer)
        total_tax += tax_amount
        
        # Update delivery counter
        deliveries_count += 1

        print(f"Tax for this delivery: {tax_amount:.2f}")
        print(f"Updated Inventory! : {inventory_init}" )
        print("\n")
        print(f"Current Inventory:  {inventory_init}")

        #python write to txt function
        # holds the updated value..
        inventory_pro_max = inventory_init

        #Save inventory data into a .txt file
        Inventory_Data = str(inventory_pro_max)

        save_file = "Inventory.txt"
        with open(save_file, 'w' , encoding="utf8") as data:
            data.write(f"This is the total inventory : {Inventory_Data}")

        if inventory_pro_max > 500: 
            print("ALERT , LOOP BROKENNN")
            break

#generate report
generate_report(inventory_pro_max, fail_reject, deliveries_count, total_tax)



