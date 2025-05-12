import random

# Define the upper bound of the guessing range
upper_bound = 100
secret_number = random.randint(1, upper_bound)

# Prompt the user to guess
while True:
    try:
        guess = int(input(f"Guess a number between 1 and {upper_bound}: "))
        if guess < 1 or guess > upper_bound:
            print(f"Please guess within the range of 1 to {upper_bound}.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the right number.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

