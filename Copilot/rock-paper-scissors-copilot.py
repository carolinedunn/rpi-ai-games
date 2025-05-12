import random

# Possible choices
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

# Run the game
play_game()
