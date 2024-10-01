# ================================
#     Understanding Input Types
# ================================

# - We use input to receive user input

# ================================
#              INPUT
# ================================

name = input("Enter your name: ")
print(name)  # Output: User input (example: 'Ana')
              # Output: Ana

# ================================
#          FLOAT, INT, AND STR
# ================================

# - If we want the user to enter numbers, we use FLOAT and INT
# - FLOAT is for decimal numbers
# - INT is for integer numbers
# - STR is used to convert NUMBERS (FLOAT AND INT) to STRING

age = int(input('Enter your age: '))  # A person can't be a fraction of a year, so we use INT
price = float(input("The product costs: "))  # An item can cost (X amount) and may include cents, so we use FLOAT
salary = float(input("Enter your salary: "))  # A person can receive a decimal amount, such as cents, so we use FLOAT

# ================================
#         Outputting Results
# ================================

# - If the numbers are not converted to STR, you will receive an error message

print("Your age is: " + str(age))  # Output: "Your age is: x"
print("The product costs: " + str(price))  # Output: "The product costs: y"
print("Your salary is: " + str(salary))  # Output: "Your salary is: z"


