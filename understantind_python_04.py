# ================================
#       Understanding Loops
# ================================

# - WHILE and FOR Loops
# - Remember Project 4
# - Understanding Lists in Python
# ================================

# Let's explore loops with a fun example!

# ================================
#             Lists
# ================================

# A list in Python is an ordered collection of items that can hold various data types, 
# such as numbers and strings. Lists are mutable, meaning you can change their elements 
# after creating them. 

# In Python, lists use zero-based indexing, meaning the first element is at position 0, 
# the second at position 1, and so on. Negative indices can be used to access elements 
# from the end of the list, with -1 being the last element.

toys = ['Little Bear', 'Ball', 'Car']  # Positions: Little Bear is 0, Ball is 1, and Car is 2

# ================================
#          Using FOR Loop
# ================================

print("Here are the toys I have:")
for toy in toys:
    print(f"I am playing with the {toy}!")  # Output: Each toy in the list is displayed: Little Bear, Ball, and Car

# Explanation of FOR Loop:
# The FOR loop iterates over each item in the 'toys' list, assigning each item to the variable 'toy' 
# one at a time. It continues this process until all items have been processed, allowing you to 
# perform actions on each item.

# ================================
#         Using WHILE Loop
# ================================

number_x = 0
print("Counting up to 5:")
while number_x < 5:
    number_x += 1
    print(f"The number is: {number_x}!")  # Output: Counts from 1 to 5

# Explanation of WHILE Loop:
# The WHILE loop continues to execute as long as the condition (number_x < 5) is true. 
# In this case, it increments 'number_x' by 1 in each iteration and prints the current value. 
# The loop stops when 'number_x' reaches 5.

