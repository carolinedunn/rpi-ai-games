import random

def number_guessing_game_with_limit(upper_limit):
    """Plays a number guessing game with a user-defined upper limit."""

    secret_number = random.randint(1, upper_limit)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {upper_limit}.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < 1 or guess > upper_limit:
                print(f"Your guess must be between 1 and {upper_limit}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    upper_limit = 20  # You can change this value to set a different upper limit
    number_guessing_game_with_limit(upper_limit)