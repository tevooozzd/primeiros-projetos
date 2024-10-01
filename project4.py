# ================================
#       Average Calculation Project
# ================================

# - Using and Understanding F-strings
# ================================

# F-strings allow you to insert Python expressions directly into strings, 
# facilitating variable interpolation and text formatting.

# Getting user input
age = int(input("Type your age: "))
print(f"Your age is: {age}")  # Output: x

# Gathering more information
name = input("Type your name: ")
rg_student = input("Type your registration: ")
proof_note = float(input("Type the note of the test: "))

# Output using f-strings for better formatting
print(f"Welcome {name}, your RG is {rg_student}, and your proof note is {proof_note}.") 
# Using f-strings makes it easier to combine variables and strings without concatenation.

# ================================
#     Average Calculation Section
# ================================

# Getting user information
name = input("Type your name: ")
print(f"Welcome to the school panel, {name}! Let's start calculating the average of your students.")

# Gathering student information
rg_student = input("Type the registration of the student: ")
test1 = float(input("Type the note of the first test: "))
test2 = float(input("Type the note of the second test: "))
test3 = float(input("Type the note of the third test: "))

# Calculating the average
average = (test1 + test2 + test3) / 3 

# Checking approval status
if average <= 6.75:
    print(f"The student {rg_student} received a note of {average:.2f} and isn't approved.")
else:
    print(f"The student {rg_student} received a note of {average:.2f} and is approved.")


