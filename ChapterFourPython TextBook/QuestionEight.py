import random


def generated_integer():
    return random.randint(1,9), random.randint(1,9)

def question():
    while True:
        num1, num2 = generated_integer()
        correct_answer = num1 * num2

        student_answer = int(input(f'how much is {num1} times {num2}? '))

        if student_answer == correct_answer:
            print('Very Good!')
            break
        else:
            print('No, please try again!')


question()