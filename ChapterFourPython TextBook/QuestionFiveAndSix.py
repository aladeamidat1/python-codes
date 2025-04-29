from functools import total_ordering


def guess_number():
    while True:
        Correct_number = 556
        print('guess the number')
        total_guessing = 0

        while True:
            guessed_number = int(input("Guess my number between 1 and 1000 with few guesses: "))
            if guessed_number > Correct_number:
                print("too high. try again.")
                total_guessing += 1
            elif guessed_number < Correct_number:
                print("too low. try again.")
                total_guessing += 1
            else:
                print(" congratulations you guessed my number!")

                if total_guessing <= 10:
                    print('you got lucky')
                else:
                    print('you should do better')
                    break
                break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            print("Thank you for playing!")
            break




guess_number()