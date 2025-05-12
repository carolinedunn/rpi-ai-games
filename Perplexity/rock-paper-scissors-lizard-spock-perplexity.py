import random

# Define the rules: what beats what
WIN_RULES = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['spock', 'paper'],
    'spock':    ['scissors', 'rock']
}

CHOICES = list(WIN_RULES.keys())

def get_user_choice():
    user_input = input(f"Enter your choice ({', '.join(CHOICES)}): ").lower()
    while user_input not in CHOICES:
        print("Invalid choice. Please try again.")
        user_input = input(f"Enter your choice ({', '.join(CHOICES)}): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif computer in WIN_RULES[user]:
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()
