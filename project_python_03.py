# ===========================================
#          Guess the Number Project
#          Using of import random
# ===========================================




# Importing necessary libraries
import random
import time

# Welcome message and getting user's name
print("================================================================================================")
print("Welcome to the guess number game!\nTo start, let's know your name...")
print("================================================================================================")
time.sleep(2)


# Getting the name
name = input("Type your name here: ")
print(f"So {name}, the game consists of my system drawing a random number between 1 and 100.\nYou just need to guess my number in 10 attempts!")
print("================================================================================================")
time.sleep(3)


# Generating a random number between 1 and 100
number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# Game loop for guessing the number
while attempts < max_attempts:
    guess = input("Guess the number: ")  # Get user input
    time.sleep(0.1)

    # Validate input
    if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
        print("This is not a valid number, or isn't a number.")
        time.sleep(1.5)
        continue  # Skip to the next iteration

    guess = int(guess)  # Convert input to integer after validation
    attempts += 1
    total = max_attempts - attempts

    # Check the guessed number against the random number
    if guess < number:
        print("===================")
        print("Too low, try again!")
        print(f"You just have {total} attempts left!")
        time.sleep(1.5)
        print("===================")
    elif guess > number:
        print("===================")
        print("Too high, try again")
        print(f"You just have {total} attempts left!")
        time.sleep(1.5)
        print("===================")
    else:
        print("===================")
        print(f"Congratulations {name}, you guessed the number! The number is {number}.")
        print(f"You just won with {total} attempts lefts!")
        time.sleep(1.5)
        break
else:
    print("===================")
    print(f"Sorry {name}, you've used all your attempts! The number was {number}.")




# ============================================
#                Explanation
# ============================================
# 1. The program starts by importing the necessary libraries: `random` for generating a random number and `time` for adding delays.
# 2. A welcome message is displayed, and the user is prompted to enter their name.
# 3. A random number between 1 and 100 is generated and stored in the variable `number`.
# 4. The user is given up to 10 attempts to guess the number.
# 5. In each iteration of the while loop, the user is asked to input their guess.
# 6. The program checks if the input is valid:
#    - It ensures that the input consists of digits only and is within the range of 1 to 100.
# 7. If the input is invalid, an error message is displayed, and the loop continues to the next iteration.
# 8. If the input is valid, it checks if the guess is lower, higher, or equal to the random number and provides feedback accordingly.
# 9. If the user guesses correctly, a congratulatory message is displayed, and the loop ends.
# 10. If the user uses all attempts without guessing correctly, a message is displayed revealing the correct number.

