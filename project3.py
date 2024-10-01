## - Understanding how to analyze user data
## - Recap of INPUT, INT, FLOAT, and STR
## - Now using data analysis (IF, ELSE, and ELSE IF)

            # Remembering INPUT, FLOAT, INT, and STR
            #   - If we want to get a response from the user, we use input()
input("Enter your name: ")
            #   - If we want to receive a response in numbers, we use INT and FLOAT before INPUT
# - Integer numbers INT
int(input("Enter your age: "))
# - Decimal numbers FLOAT
float(input("Enter the product value: "))
# - Convert these numerical values to string
str(variable)

            # - Data analysis
            #   - Let's take user data and check if they are eligible to perform a certain action

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
product = float(input("The product value is: "))

if age < 18:
    print("You are a minor and cannot make this purchase!")
elif product > salary:
    print("You do not have enough salary, we are sorry, please come back later!")
else: 
    result = salary - product
    print("You can make the purchase and will have R$" + str(result) + " left from your salary!")

#                                 Explanation
# 1 - It will take the user's inputs
# 2 - If the user is under 18, print1 will appear; if they are older, it will continue
# 3 - It will check their salary and the product value; if the product value is greater, print2 will return (since you cannot buy something without the money)
# 4 - If the salary is greater than the product value, it will calculate (salary - product), and print3 will show how much is left
