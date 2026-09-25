print("=======================================================================")
print("Smart Inventory Auditor")
print("=======================================================================")

FILE_PATH = "Inventory.txt"

# 1 & 4. Load Inventory on Startup
def load_inventory():
    try:
        with open(FILE_PATH, 'r', encoding="utf8") as data:
            content = data.read().strip()
            print("Existing inventory record loaded successfully.")
            
            # Extract number from format: "Total Inventory: X"
            for line in content.splitlines():
                if "Total Inventory:" in line:
                    number_part = line.split(":")[-1].strip()
                    if number_part.isdigit():
                        return int(number_part)
            return 0
    except FileNotFoundError:
        print("No existing inventory file found. Starting with empty inventory.")
        return 0

# 3 & 4. Save Total and History List to file
def save_inventory(final_total, history_list):
    with open(FILE_PATH, 'w', encoding="utf8") as data:
        data.write(f"Total Inventory: {final_total}\n")
        data.write(f"Transaction History: {history_list}\n")
    print("Final total and history successfully saved to Inventory.txt")

# Input Validation
def get_valid_input():
    user_input = input("Enter Stock Quantity  :")
    
    if user_input == "":
        print("Please type something....")
        return None
    elif user_input.isdigit():
        return int(user_input)
    elif user_input.lower() == "quit":
        return "quit"
    else:
        print("Invalid Input")
        return None

# Process Delivery Total
def process_delivery(current_total, new_value):
    return current_total + new_value

# Calculate 10% Tax
def calculate_tax(amount):
    return amount * 0.10

# Generate Report
def generate_report(total_units, failed_attempts, total_deliveries, total_tax, history_list):
    print("\n=======================================================================")
    print("Summary")
    print("=======================================================================")
    print(f"Total Units Processed             : {total_units}")
    print(f"Total Deliveries Processed        : {total_deliveries}")
    print(f"Total Tax (10%)                   : {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries : {failed_attempts}")
    print(f"Transaction History               : {history_list}")
    print("=======================================================================")


# Initialize values
inventory_init = load_inventory()  # Load previous saved total
history_tracking = []              # 2. List to track valid entries
fail_reject = 0
deliveries_count = 0
total_tax = 0.0

# Main loop
while True:
    validated_input = get_valid_input()

    if validated_input == "quit":
        print("Successfully exited the programme")
        break

    elif validated_input is None:
        fail_reject += 1

    else:
        integer = validated_input
        
        # 2. Record valid transaction to history list
        history_tracking.append(integer)
        
        inventory_init = process_delivery(inventory_init, integer)
        tax_amount = calculate_tax(integer)
        total_tax += tax_amount
        deliveries_count += 1

        print(f"Tax for this delivery: {tax_amount:.2f}")
        print(f"Updated Inventory! : {inventory_init}")
        print(f"Current Inventory:  {inventory_init}\n")

        if inventory_init > 500: 
            print("ALERT, Inventory limit exceeded! Stopping loop.")
            break

# 3. Write-back on exit (Save total and history list)
save_inventory(inventory_init, history_tracking)

# Generate final report
generate_report(inventory_init, fail_reject, deliveries_count, total_tax, history_tracking)