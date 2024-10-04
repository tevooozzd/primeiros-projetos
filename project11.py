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


physics_questions = {
    "What is the law of universal gravitation?": "b",
    "What is the unit of force in the International System?": "a",
    "What defines the velocity of an object?": "c",
    "What is the difference between mass and weight?": "d",
    "What is kinetic energy?": "a",
    "What happens when you increase the temperature of a gas, keeping its volume constant?": "b",
    "What do you call the change of state from liquid to gas?": "a"
}

physics_options = {
    "What is the law of universal gravitation?": "A) Forces between electric charges   B) Forces between masses   C) Forces between atoms   D) Forces between liquids",
    "What is the unit of force in the International System?": "A) Newton   B) Joule   C) Pascal   D) Watt",
    "What defines the velocity of an object?": "A) Distance   B) Time   C) Distance and time   D) Mass",
    "What is the difference between mass and weight?": "A) Mass is force   B) Weight is a measure of matter   C) Mass is constant and weight varies with gravity   D) There is no difference",
    "What is kinetic energy?": "A) Energy of motion   B) Potential energy   C) Thermal energy   D) Electrical energy",
    "What happens when you increase the temperature of a gas, keeping its volume constant?": "A) Pressure decreases   B) Pressure increases   C) Volume increases   D) Temperature does not change",
    "What do you call the change of state from liquid to gas?": "A) Vaporization   B) Condensation   C) Sublimation   D) Solidification"
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

print("Physics Quiz:")
quiz(physics_questions, physics_options)
