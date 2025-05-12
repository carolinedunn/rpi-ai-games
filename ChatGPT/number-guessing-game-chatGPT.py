import random

def number_guessing_game():
    upper_limit = 10  # You can change this to any number you want
    number_to_guess = random.randint(1, upper_limit)
    attempts = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {upper_limit}.")

    while True:
        try:
            user_guess = int(input(f"Take a guess (1-{upper_limit}): "))
            attempts += 1

            if user_guess < 1 or user_guess > upper_limit:
                print(f"Please enter a number between 1 and {upper_limit}.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("That's not a valid number. Please enter an integer.")

# Run the game
number_guessing_game()
