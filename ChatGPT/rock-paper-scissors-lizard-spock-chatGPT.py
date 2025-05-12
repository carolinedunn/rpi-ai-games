import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_input = input("Enter rock, paper, scissors, lizard, or spock: ").lower()
    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Enter rock, paper, scissors, lizard, or spock: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

def determine_winner(user, computer):
    winning_combos = {
        'rock':     ['scissors', 'lizard'],
        'paper':    ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard':   ['spock', 'paper'],
        'spock':    ['scissors', 'rock']
    }

    if user == computer:
        return "It's a tie!"
    elif computer in winning_combos[user]:
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play()
