#ACTIVTY 1 (first post) / #ACTIVITY 2  (Fun conditions)
print("===============")
print("Welcome here!")
print("This is my first post")
print("===============")


username = "Im_am_a_SITstudent"
bio = "Student"
followers = 67

#
#ACTIVITY 3  (Assignment Variables)
followers += 6767
print("Day 1:", followers)

followers += 6700
print("Day 2:", followers)

followers -= 5900
print("Day 3:", followers)

#This will print the username
print("Username:", username)

#This will print the bio
print("Bio:", bio)

#This will print the amount of followers
print("Followers:", followers)


#ACTIVITY 4  (Dynamic Profile) /#ACTIVITY 5 (Fun Conditions)
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Catogory: ")


print("====================")
print("\nInstagram Profile")
print("====================")
print("Username: ", username)
print("Age: ", age)
print("Category:", category)


if age>40 and category == "fun":
    print("How old is fun for you??")



#git commit acts as a save point so i can go back to this file if i mess up later on, 
#meaning i can go back to this version 

#git commit -m "First Post" is just a brief note of what changes were made in this 
#specific point of time

# Step 1 #
# git add xxx.py

# Step 2 #
# git commit -m "xxxx.py"

# Step 3 #
# Use git log to see the history of changes