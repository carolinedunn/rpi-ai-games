import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Let the user choose the upper limit
    while True:
        try:
            upper_limit = int(input("Please enter the upper limit (must be an integer greater than 1): "))
            if upper_limit <= 1:
                print("The upper limit must be greater than 1. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    print(f"I have chosen a number between 1 and {upper_limit}. Can you guess what it is?")
    
    secret_number = random.randint(1, upper_limit)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input(f"Enter your guess (between 1 and {upper_limit}): "))
            if user_guess < 1 or user_guess > upper_limit:
                print(f"Please enter a number between 1 and {upper_limit}.")
                continue
            
            attempts += 1
            
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
number_guessing_game()
