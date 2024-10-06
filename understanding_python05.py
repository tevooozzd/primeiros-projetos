# - Rebember WHILE, FOR
# Do a timer project
# Understanding and use import



# ==========================================
#         Understanding IMPORT
# ================================

# - The `import` statement is used to bring in external modules and libraries into your Python code.
# - This allows you to use pre-built functions, classes, and variables defined in those modules.








# =========================================
#          Remember FOR and WHILE to Loop
# =========================================

print("Counting with FOR loop:")
for number in range(6):  # Counts from 0 to 5
    print(f"Number: {number}")



print("Counting with WHILE loop:")
count = 1
while count <= 5:  # Counts from 1 to 5
    print(f"Number: {count}")
    count += 1

# ================================
#       Countdown timer project
# ==========================================


import time
print("Let's start to use the timer!")
timer = int(input("Type the time that you want (in seconds): "))


while timer > 0:
    print(f"{timer}, seconds remains...")
    time.sleep(1)
    timer -= 1
print("Times's UP!")    


# ==========================================
# Explanation of the Project
# ==========================================
# This project demonstrates the use of loops and imports in Python.
# It starts with counting using both a FOR loop (counting from 0 to 5)
# and a WHILE loop (counting from 1 to 5). 
# The program then implements a countdown timer, where the user inputs a time in seconds. 
# The timer counts down, displaying the remaining seconds every second 
# until it reaches zero, at which point it displays "Time's UP!".
