def motivational_message(msg):
    print("You can", msg)

motivational_message("Keep striving!")
# Should print: You can! Keep striving!

def error_message(err):
    print("Error", err, "Try again")

error_message(404)
# Should print: Error 404: Try again!

def birthday_message(name, age):
    print(f"Happy birthday, {name}! You are now {age} years old!")

birthday_message("Ana", 10)
# Should print: Happy birthday, Ana! You are now 10 years old!

def welcome_message(name):
    print(f"Hello, {name}! Great to see you!")

welcome_message("Carlos")
# Should print: Hello, Carlos! Great to see you!

def thank_you_message(name, task):
    print(f"Thank you, {name}, for {task}")

thank_you_message("Mariana", "helping with the task")
# Should print: Thank you, Mariana, for helping with the task!

def alert_message(alert):
    print(f"Attention: {alert}")

alert_message("heavy rain ahead")
# Should print: Attention: heavy rain ahead!

def goodbye_message(name):
    print(f"Goodbye, {name}! See you later!")

goodbye_message("Luiz")
# Should print: Goodbye, Luiz! See you later!

def count_words(sentence):
    words = sentence.split()
    return len(words)

result = count_words(input("Type your sentence here: "))
print(result)
# Should return: 5
