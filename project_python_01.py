########################################
#
#       Average calculation project
#
########################################





#####################################################################################
name = input("Type your name: ")
age = int(input("Type your age: "))
rg_people = input("Type your registrations school: ")
notes = []




#####################################################################################
def welcome(nm, ag):
    if ag >= 18:
        print(f"Hello {name}, welcome to the calculate average project (college): ")
    elif ag >= 15:
        print(f"Hello {name}, welcome to the calculate average project (high-school): ")
    else:
        print(f"Hello {name}, welcome to the calculate average project (school): ")
        
welcome(name, age)




#####################################################################################
def registration(rg):
    if rg[:2] != '00':

        print(f"Welcome {name}, you're a student!")

        for i in range(3):
            notes_student = float(input("Type the note of the student: "))
            notes.append(notes_student)
    else:
        print(f"Welcome {name}, you're a teacher!")

        rg_student = input("Type the registration of the student: ")
        print(f"Adding notes for student with registration {rg_student}.")
        for i in range(3):
            notes_student = float(input("Type the note of the student: "))
            notes.append(notes_student)
            
registration(rg_people)




#####################################################################################
if notes:
    average = sum(notes) / len(notes)
    print(f"The average of the notes is: {average}")
    if average >= 70:
        print(f" CONGRATULATIONS, APRROVED! ")
    else:
        print(f"So sorry, didn't pass :(")
else:
    print("No notes were entered.")
#####################################################################################



# ================================
#            Explanation
# ================================

# This code creates a simple calculator that performs addition, subtraction, multiplication,
# division, or potentiation based on user input. It uses IF, ELIF, and ELSE statements to
# determine which operation to perform, and it imports the time module to introduce pauses
# for a smoother user experience. Each operation prompts the user for two numbers, then
# calculates and displays the result.

