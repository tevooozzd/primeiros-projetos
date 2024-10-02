# ==================================================
#          UNIT CONVERTER Project
#          Using import time and sys
#          Understanding methods in Python
# ==================================================

# Importing necessary libraries
import time  # To add delays in the program
import sys   # To exit the program

# Welcome message and getting user's name
print("================================================================================================")
print("Welcome to the UNIT CONVERTER project!\nTo start, let's know your name...")
print("================================================================================================")
time.sleep(1.3)  # Pause for 1.3 seconds

# Getting user's name
name = input("Type your name here: ")  # Get the user's name
print(f"So {name}, let's start")  # Greet the user
print("================================================================================================")
time.sleep(1.3)

# Presenting options for unit conversion
print("Type the number corresponding to the operation you want: \n"
      "Length - 1\n"
      "Temperature - 2\n"
      "Capacity - 3\n"
      "Mass - 4\n"
      "Volume - 5\n")

# Getting the user's choice for conversion operation
convert_operation = input("What operation do you want to do?: ")
while not convert_operation.isdigit() or not (1 <= int(convert_operation) <= 5):
    print("This is not an option OR not a number! Please try again.")
    time.sleep(0.8)
    convert_operation = input("What operation do you want to do?: ")

print(f"So {name}, you chose option {convert_operation}, let's start!")

# Length conversion
if convert_operation == '1':
    print('==================================================================')
    print("In this case of UNIT LENGTH, you will choose TWO (2) units. The first will be converted to the second. What do you prefer?")
    print("Millimeter (mm) - 1\n"
          "Centimeter (cm) - 2\n"
          "Meter (m) - 3\n"
          "Kilometer (km) - 4\n")
    
    # Getting user's choices for conversion
    operationc1 = input("Choose one option to convert from: ")
    operationc2 = input("Choose the second option to convert to: ")
    value = float(input("Now, type the quantity you want to be converted: "))

    # Validate that the two selected units are not the same
    while operationc1 == operationc2 or value == '':
        print("You can't use the same unit. Try again or enter a valid value!")
        operationc1 = input("Choose one option to convert from: ")
        operationc2 = input("Choose the second option to convert to: ")

    # Perform the conversions based on user selections
    if operationc1 == '1' and operationc2 == '2':
        result = value / 10
        print(f"So {name}, your operation result is {result} centimeters.")
        sys.exit()
    elif operationc1 == '1' and operationc2 == '3':
        result = value / 1000
        print(f"So {name}, your operation result is {result} meters.")
        sys.exit()
    elif operationc1 == '1' and operationc2 == '4':
        result = value / 1000
        print(f"So {name}, your operation result is {result} kilometers.")
        sys.exit()
    elif operationc1 == '2' and operationc2 == '1':
        result = value * 10
        print(f"So {name}, your operation result is {result} millimeters.")
        sys.exit()
    elif operationc1 == '2' and operationc2 == '3':
        result = value / 100
        print(f"So {name}, your operation result is {result} meters.")
        sys.exit()
    elif operationc1 == '2' and operationc2 == '4':
        result = value / 100000
        print(f"So {name}, your operation result is {result} kilometers.")
        sys.exit()
    elif operationc1 == '3' and operationc2 == '1':
        result = value * 1000
        print(f"So {name}, your operation result is {result} millimeters.")
        sys.exit()
    elif operationc1 == '3' and operationc2 == '2':
        result = value * 100
        print(f"So {name}, your operation result is {result} centimeters.")
        sys.exit()
    elif operationc1 == '3' and operationc2 == '4':
        result = value / 1000
        print(f"So {name}, your operation result is {result} kilometers.")
        sys.exit()
    elif operationc1 == '4' and operationc2 == '1':
        result = value * 1000000
        print(f"So {name}, your operation result is {result} millimeters.")
        sys.exit()
    elif operationc1 == '4' and operationc2 == '2':
        result = value * 100000
        print(f"So {name}, your operation result is {result} centimeters.")
        sys.exit()
    elif operationc1 == '4' and operationc2 == '3':
        result = value / 1000
        print(f"So {name}, your operation result is {result} meters.")
        sys.exit()






# ============================================
#                Explanation
# ============================================
# 1. The program begins by importing the necessary libraries: `time` for adding delays,
#    and `sys` for program termination.
# 2. A welcome message is displayed, prompting the user to enter their name.
# 3. The user is presented with a menu of conversion options (length, temperature, capacity, mass, volume).
# 4. The program validates the user's choice to ensure it's a valid option.
# 5. If the user selects length conversion, they are prompted to choose two units to convert between.
# 6. The program checks that the selected units are not the same and validates the input value.
# 7. Based on the user's selections, the program performs the appropriate conversion calculations.
# 8. The result is displayed to the user, and the program exits.
