print("=======================================================================")
print("Smart Inventory Auditor")
print("=======================================================================")

#step 1 (Initialize inventory to 0)
inventory_init = 0

fail_reject = 0

inventory_pro_max = 0


#step 2 continuous loop asking user to enter a stock quantity, until the user types quit
for x in range(0,10):
    user_input = input("Enter Stock Quantity  :")

    if user_input == "":
       print("Please type something....")

    #step 3,4,5,6
    #return true if the string is a digit string, if not its false
    #isdigit Returns True if all characters in the string are digits
    #isdigit automatically reject -ve numbers
    elif user_input.isdigit():
        #convert str(user_input) type into int type
        integer = int(user_input)

        #add on to the 0 which came from inventory_init
        inventory_init += integer

        print(f"Updated Inventory! : {inventory_init}" )
        print("\n")
        print(f"Current Inventory:  {inventory_init}")

        #holds the updated value..
        inventory_pro_max = inventory_init

        if inventory_pro_max > 500: 
            print("ALERT , LOOP BROKENNN")
            break
        



    elif user_input == "quit" or user_input == "QUIT":

        print("Successfully exited the programme")
        print("Summary")
        print("\n")
        print(f"Total Units Processed :  {inventory_pro_max} ")
        print(f"Number of Failed/Rejected Entries   : {fail_reject}  " )
        break        

    else:
        print("Invalid Input")
        fail_reject += 1

    