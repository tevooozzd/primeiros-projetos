
# ================================
#         IMPORTANT ALERT
# ================================


# I know this could be simplified in code, but I'm trying to understand step by step how 
# Python works. For this, I used more code and lines. I know this is extra work, and in 
# future projects, I will use less :/






















# ================================
#          Multiplication Project
# ================================

# - Using IF, ELIF, and ELSE
# - Using WHILE and FOR
# - Importing TIME
# - Using \n and \t for formatting

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

# Perform chosen operation
if to_choose == 1:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number you want to add: "))
    number_two = float(input("Type the second number you want to add: "))
    result = number_one + number_two
    print('================================================')
    print(f"The addition of {number_one} + {number_two} is {result}")
elif to_choose == 2:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number you want to subtract: "))
    number_two = float(input("Type the second number you want to subtract: "))
    result = number_one - number_two
    print('================================================')
    print(f"The subtraction of {number_one} - {number_two} is {result}")
elif to_choose == 3:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number you want to multiply: "))
    number_two = float(input("Type the second number you want to multiply: "))
    result = number_one * number_two
    print('================================================')
    print(f"The multiplication of {number_one} * {number_two} is {result}")
elif to_choose == 4:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number you want to divide: "))
    number_two = float(input("Type the second number you want to divide: "))
    result = number_one / number_two
    print('================================================')
    print(f"The division of {number_one} / {number_two} is {result}")
elif to_choose == 5:
    print(f"So... you chose {to_choose}, let's start")
    print('================================================')
    number_one = float(input("Type the first number you want to raise: "))
    number_two = float(input("Type the second number you want to raise: "))
    result = number_one ** number_two
    print('================================================')
    print(f"The potentiation of {number_one} ** {number_two} is {result}")
else:
    print(f"Sorry {name}, that number isn't valid!")

# ================================
#            Explanation
# ================================

# This code creates a simple calculator that performs addition, subtraction, multiplication,
# division, or potentiation based on user input. It uses IF, ELIF, and ELSE statements to
# determine which operation to perform, and it imports the time module to introduce pauses
# for a smoother user experience. Each operation prompts the user for two numbers, then
# calculates and displays the result.

