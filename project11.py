# Questions and answers for Mathematics
math_questions = {
    "What is the square root of 144?": "c",
    "What is the formula to calculate the area of a circle?": "a",
    "If a triangle has sides of 3 cm, 4 cm, and 5 cm, is it a triangle?": "a",
    "What is the result of '15%' of 200?": "b",
    "What is the sum of the internal angles of a square?": "d",
    "What does the hypotenuse represent in a right triangle?": "a",
    "What do you call a sequence of numbers where each number is the sum of the two preceding ones?": "b"
}

math_options = {
    "What is the square root of 144?": "A) 10    B) 11    C) 12    D) 13",
    "What is the formula to calculate the area of a circle?": "A) A=πr    B) Y=mx + b     C) A + B + C    D) P = 4l",
    "If a triangle has sides of 3 cm, 4 cm, and 5 cm, is it a triangle?": "A) Right    B) Isosceles    C) Scalene    D) Square",
    "What is the result of '15%' of 200?": "A) 60    B) 30    C) 15    D) 5.75",
    "What is the sum of the internal angles of a square?": "A) 40 degrees   B) 50 degrees   C) 180 degrees  D) 360 degrees",
    "What does the hypotenuse represent in a right triangle?": "A) longest side of the triangle    B) Nothing   C) The side of the angle   D) The shortest side",
    "What do you call a sequence of numbers where each number is the sum of the two preceding ones?": "A) Pythagorean   B) Fibonacci Sequence   C) Bhaskara  D) Physical Algebra"
}


def quiz(questions, options):
    correct_answers = 0
    incorrect_answers = 0

    for question in questions:
        print(question)
        print(options[question])
        
        answer = input("Which option is the answer (a, b, c, d): ").lower()
        
        while answer not in ['a', 'b', 'c', 'd']:
            print("That is not an option! Let's try again!")
            answer = input("Which option is the answer (a, b, c, d): ").lower()

        if answer == questions[question]:
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong!")
            incorrect_answers += 1

        print(f"You have {correct_answers} correct answers and {incorrect_answers} wrong answers.")
        print()


print("Math Quiz:")
quiz(math_questions, math_options)

