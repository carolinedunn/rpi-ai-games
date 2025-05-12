import random

def number_guessing_game(upper_limit=10):
    # Generate a random number between 1 and the upper limit
    secret_number = random.randint(1, upper_limit)
    attempts = 0
    max_attempts = 3
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {upper_limit}.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            
            # Validate input
            if guess < 1 or guess > upper_limit:
                print(f"Please enter a number between 1 and {upper_limit}.")
                continue
                
            # Count the attempt
            attempts += 1
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
                
            # Inform player of remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")
            else:
                print(f"Game over! The number was {secret_number}.")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    # Ask the user for the upper limit
    try:
        custom_limit = int(input("Enter the maximum number for the game (default is 10): "))
        if custom_limit < 2:
            print("Upper limit must be at least 2. Setting to default value of 10.")
            custom_limit = 10
    except ValueError:
        print("Invalid input. Using default upper limit of 10.")
        custom_limit = 10
    
    # Start the game with the custom upper limit
    number_guessing_game(custom_limit)
    
    # Ask if the player wants to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            try:
                change_limit = input("Do you want to change the upper limit? (yes/no): ").lower()
                if change_limit in ["yes", "y"]:
                    try:
                        custom_limit = int(input(f"Enter the maximum number for the game (current: {custom_limit}): "))
                        if custom_limit < 2:
                            print("Upper limit must be at least 2. Keeping previous value.")
                    except ValueError:
                        print("Invalid input. Keeping previous upper limit.")
            except:
                pass
            number_guessing_game(custom_limit)
        elif play_again in ["no", "n"]:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")