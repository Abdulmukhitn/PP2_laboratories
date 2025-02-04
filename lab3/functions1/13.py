import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 20. Try to guess it!")


    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

guess_the_number()
