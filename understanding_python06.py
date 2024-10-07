def motivational_message(msg):
    print("You can", msg)

motivational_message("Keep striving!")
################################################################




def error_message(err):
    print("Error", err, "Try again")

error_message(404)
motivational_message("Keep striving!")
################################################################




def birthday_message(name, age):
    print(f"Happy birthday, {name}! You are now {age} years old!")

birthday_message("Ana", 10)
motivational_message("Keep striving!")
################################################################




def welcome_message(name):
    print(f"Hello, {name}! Great to see you!")

welcome_message("Carlos")
motivational_message("Keep striving!")
################################################################




def thank_you_message(name, task):
    print(f"Thank you, {name}, for {task}")

thank_you_message("Mariana", "helping with the task")
motivational_message("Keep striving!")
################################################################




def alert_message(alert):
    print(f"Attention: {alert}")

alert_message("heavy rain ahead")
motivational_message("Keep striving!")
################################################################




def goodbye_message(name):
    print(f"Goodbye, {name}! See you later!")

goodbye_message("Luiz")
motivational_message("Keep striving!")
################################################################




def count_words(sentence):
    words = sentence.split()
    return len(words)

result = count_words(input("Type your sentence here: "))
print(result)
motivational_message("Keep striving!")
################################################################




import os

user_input = float(input("Type the fisrt number: "))
user_input2 = float(input("Type the second number: "))
def two_numbers(a, b):
    return a + b

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


print(f"The result is : {two_numbers(user_input, user_input2)}")
################################################################




user_input3 = int(input("Type the number: "))

def result(number):
    if number % 2 == 0:
        return "even number"
    else:
        return "odd"

print(result(user_input))
################################################################




user_input4 = int(input("Type the number that you want to know the multiplication table: "))

def mul_table(x):
    for y in range(1, 11):
        print(f"{x} × {y} = {x * y}")

mul_table(user_input)
################################################################




user_input = input("Type the word that you want to see if it's a polindrome: ")

def word(x):
    if x == ''.join(reversed(x)):
        print("It's a palindrome")
    else:
        print("Isn't a palindrome")
        
word(user_input)
################################################################




my_list = []

def addlist(x): 
    my_list.append(x)

for i in range(10):
    user_input = input("Type numbers to the list: ")
    addlist(user_input)  

my_list.sort() 
print("Sorted list:", my_list)
##############################################################

