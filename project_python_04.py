# ==================================================
#          Generate Password Project
#          Using import random, string and time
#          Using and understand methods in python
# ==================================================




# Importing necessary libraries
import time  # To add delays in the program
import random  # For generating random choices
import string  # For accessing string constants like letters and digits





# Welcome message and getting user's name
print("================================================================================================")
print("Welcome to the generate password project!\nTo start, let's know your name...")
print("================================================================================================")
time.sleep(1.3)  # Pause for 2 seconds
name = input("Type your name here: ")  # Get the user's name
print(f"So {name}, let's start")  # Greet the user
print("================================================================================================")




# Preparing to collect character options for the password
characters = ''  
password_length = input("Enter the number of characters you want in your password: ")




# Loop until a valid number is entered
while not password_length.isdigit():
    print("You typed an answer that's INVALID, let's try again!")
    time.sleep(0.7)
    password_length = input("Enter the number of characters you want in your password: ")
password_length  = int(password_length)




# Asking the user if they want lowercase letters
print('=====================================================================')
lowercase = input("Do you want lowercase letters? (Answer with y or n): ")  # Ask for lowercase letters
if lowercase == 'y':
    characters += string.ascii_lowercase  # Add lowercase letters to the character set
    print("Ok, Let's continue...")
    time.sleep(0.7)
elif lowercase == 'n':
    print("Ok, Let's continue...")
else:
    print("This is not a valid option, so the answer is 'n' ")  # Handle invalid input


# Asking the user if they want uppercase letters
print('=====================================================================')
uppercase = input("Do you want uppercase letters? (Answer with y or n): ")  # Ask for uppercase letters
if uppercase == 'y':
    characters += string.ascii_uppercase  # Add uppercase letters to the character set
    print("Ok, Let's continue...")
    time.sleep(0.7)
elif uppercase == 'n':
    print("Ok, Let's continue...")
else:
    print("This is not a valid option, so the answer is 'n' ")  # Handle invalid input


# Asking the user if they want numbers
print('=====================================================================')
numbers = input("Do you want numbers? (Answer with y or n): ")  # Ask for numbers
if numbers == 'y':
    characters += string.digits  # Add digits to the character set
    print("Ok, Let's continue...")
    time.sleep(0.7)
elif numbers == 'n':
    print("Ok, Let's continue...")
else:
    print("This is not a valid option, so the answer is 'n' ")  # Handle invalid input


# Asking the user if they want symbols
print('=====================================================================')
symbols = input("Do you want symbols? (Answer with y or n): ")  # Ask for symbols
if symbols == 'y':
    characters += string.punctuation  # Add punctuation symbols to the character set
    print("Ok, Let's continue...")
    time.sleep(0.7)
elif symbols == 'n':
    print("Ok, Let's continue...")
else:
    print("This is not a valid option, so the answer is 'n' ")  # Handle invalid input




while not characters:
    print('=====================================================================') 
    print(f"Hey {name}, your password cannot be generated because you need to choose at least one option. Let's try again!")
    time.sleep(1)
    break  # This will just break the loop without re-asking

# Generate password if characters have been selected
if characters:
    password = ''.join(random.choice(characters) for _ in range(password_length))  # Create password
    print(f"Hey {name},\nyour password with:\n{lowercase.upper()} for lowercase letters,\n{uppercase.upper()} for uppercase letters,\n{numbers.upper()} for numbers, and\n{symbols.upper()} for symbols,\nwith a length of {password_length} is:\n\n{password}")  # Display the password
else:
    print("You must select at least one type of character to generate a password.")








# ============================================
#                Explanation
# ============================================
# 1. The program starts by importing the necessary libraries: `time` for adding delays,
#    `random` for generating random choices, and `string` for accessing predefined string constants.
# 2. A welcome message is displayed, and the user is prompted to enter their name.
# 3. The user is asked for the desired length of the password.
# 4. The program then prompts the user to choose character types for the password: lowercase, uppercase, numbers, and symbols.
# 5. Each response is validated, and the appropriate character set is added to the `characters` variable.
# 6. Finally, the password is generated using random choices from the selected character set, and the result is displayed.
