import time

# Welcome message
print("Welcome to the panel! To start, type your name...")
time.sleep(1)

# Get the name
name = input("Type your name: ")
time.sleep(0.5)
print('================================================')
# Message to choose an operation
print(f"So... Let's start {name}, choose an option to continue...")

print("Type the number corresponding to the operation you want:\n"
    "Addition - 1\n"
    "Subtraction - 2\n"
    "Multiplication - 3\n"
    "Division - 4\n"
    "Potentiation - 5")
time.sleep(2)
print('=============================================================')
# Get user's choice
to_choose = int(input("Type the operation by the number: "))



def calculate_op(operation, n1, n2):
    if operation == 1:
        return n1 + n2
    elif operation == 2:
        return n1 - n2
    elif operation == 3:
        return n1 * n2
    elif operation == 4:
        return n1 / n2
    elif operation == 5:
        return n1 ** n2


if 1 <= to_choose <= 5:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number: "))
    number_two = float(input("Type the second number: "))
    result = calculate_op(to_choose, number_one, number_two)
    print('================================================')
    operations = ["addition", "subtraction", "multiplication", "division", "potentiation"]
    print(f"The result of {operations[to_choose - 1]} is: {result}")
else:
    print(f"Sorry {name}, that number isn't valid!")
