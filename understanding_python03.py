# ================================
#      Understanding User Data Analysis
# ================================

# - Recap of INPUT, INT, FLOAT, and STR
# ================================

# If we want to get a response from the user, we use input()
user_name = input("Enter your name: ")

# If we want to receive a response in numbers, we use INT and FLOAT before INPUT
# - Integer numbers INT
age = int(input("Enter your age: "))
# - Decimal numbers FLOAT
salary = float(input("Enter your salary: "))
product = float(input("The product value is: "))

# ================================
#           Data Analysis
# ================================

# Let's take user data and check if they are eligible to perform a certain action
if age < 18:
    print("You are a minor and cannot make this purchase!")
elif product > salary:
    print("You do not have enough salary. We are sorry, please come back later!")
else: 
    remaining_balance = salary - product
    print(f"You can make the purchase and will have R${remaining_balance:.2f} left from your salary!")

# ================================
#           Explanation
# ================================

# 1 - It takes the user's inputs.
# 2 - If the user is under 18, a message will be printed; if they are older, it will continue.
# 3 - It checks their salary against the product value; if the product value is greater, a message will be printed (you cannot buy something without the money).
# 4 - If the salary is greater than the product value, it calculates (salary - product) and shows how much is left.


