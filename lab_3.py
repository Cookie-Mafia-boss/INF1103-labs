def get_valid_input():

    fail_reject = 0
    current_inventory = 0

    while True:
        user_input = input("Enter Stock Quantity  :")

        if user_input == "":
            print("Please type something....")

        elif user_input.isdigit():
            integer = int(user_input)
            current_inventory += integer

            print(f"Updated Inventory! : {current_inventory}")
            print("\n")
            print(f"Current Inventory: {current_inventory}")

            if current_inventory > 500:
                print("ALERT, LOOP BROKENNN")

                # Return BOTH values
                return(current_inventory, fail_reject)

        elif user_input == "quit" or user_input == "QUIT":
            print("Successfully exited the programme")
            print("Summary")
            print("\n")
            print(f"Total Units Processed : {current_inventory}")
            print(f"Number of Failed/Rejected Entries : {fail_reject}")

            # Return BOTH values
            return(current_inventory, fail_reject)

        else:
            print("Invalid Input")
            fail_reject += 1


def process_delivery(current_total, new_value):

    current_total -= new_value

    if current_total == 0:
        print("INVALID")

    return(current_total)


def calculate_tax(amount):

    # 10 percent from delivery amount
    amount = 0.1 * amount

    return(amount)


def generate_report(total_units, failed_attempts):

    print("REPORT--")
    print(f"These are the total units {total_units}")
    print(f"These are the failed attempts {failed_attempts}")

    return(total_units, failed_attempts)

current_inventory, fail_reject = get_valid_input()

delivery_input = input("Delivery amount from Current Inventory : ")

if delivery_input.isdigit():

    new_value = float(delivery_input)

    # current_inventory goes into current_total
    new_delivery = process_delivery(current_inventory, new_value)

    print(f"Amount of units left in Inventory : {new_delivery}")
    
    tax = delivery_input

    print(f"Taxable amount from deliveries : {tax}")

else:
    print("Invalid input")



total_units, failed_attempts = generate_report(current_inventory,fail_reject)

print(total_units, failed_attempts)