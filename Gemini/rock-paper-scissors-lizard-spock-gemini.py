import random

def play_rpsls():
    """Plays a game of Rock, Paper, Scissors, Lizard, Spock with the user."""

    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_choice = random.choice(choices)

    # Rules of the game
    rules = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"],
    }

    while True:
        user_choice = input("Choose rock, paper, scissors, lizard, or spock: ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please enter rock, paper, scissors, lizard, or spock.")

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice in rules and computer_choice in rules[user_choice]:
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    play_rpsls()