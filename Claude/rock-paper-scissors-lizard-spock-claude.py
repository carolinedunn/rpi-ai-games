import random
import time

def print_rules():
    """Display the rules of Rock Paper Scissors Lizard Spock."""
    print("\n=== RULES ===")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print("=============\n")

def get_user_choice():
    """Get and validate the user's choice."""
    valid_choices = ['rock', 'paper', 'scissors', 'lizard', 'spock', 'quit', 'rules']
    
    while True:
        print("\nChoose: rock, paper, scissors, lizard, spock (or 'rules' for rules, 'quit' to exit)")
        user_choice = input("Your choice: ").lower().strip()
        
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generate the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie", ""
    
    # Define all winning relationships
    # Format: {choice: [what it beats, with what action]}
    winning_combinations = {
        'scissors': [('paper', 'cuts'), ('lizard', 'decapitates')],
        'paper': [('rock', 'covers'), ('spock', 'disproves')],
        'rock': [('lizard', 'crushes'), ('scissors', 'crushes')],
        'lizard': [('spock', 'poisons'), ('paper', 'eats')],
        'spock': [('scissors', 'smashes'), ('rock', 'vaporizes')]
    }
    
    # Check if user wins
    for beaten_choice, action in winning_combinations[user_choice]:
        if beaten_choice == computer_choice:
            return "user", f"{user_choice.capitalize()} {action} {computer_choice}"
    
    # If we get here, computer wins
    for beaten_choice, action in winning_combinations[computer_choice]:
        if beaten_choice == user_choice:
            return "computer", f"{computer_choice.capitalize()} {action} {user_choice}"

def display_result(user_choice, computer_choice, winner, win_description):
    """Display the result of the round."""
    print(f"\nYou chose: {user_choice.capitalize()}")
    print("Computer is thinking...")
    time.sleep(1)
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{win_description}!")
        if winner == "user":
            print("You win!")
        else:
            print("Computer wins!")

def play_game():
    """Main game loop."""
    user_score = 0
    computer_score = 0
    ties = 0
    
    print("=== ROCK PAPER SCISSORS LIZARD SPOCK ===")
    print("As Sheldon explains: \"Scissors cuts paper, paper covers rock, rock crushes lizard,")
    print("lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,")
    print("lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has,")
    print("rock crushes scissors.\"")
    print("\nBest out of 5 rounds wins the game!")
    
    round_num = 1
    
    while True:
        print(f"\n--- Round {round_num} ---")
        print(f"Score: You {user_score} - {computer_score} Computer (Ties: {ties})")
        
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            break
        elif user_choice == 'rules':
            print_rules()
            continue
            
        computer_choice = get_computer_choice()
        winner, win_description = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner, win_description)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            ties += 1
            
        round_num += 1
        
        # Check if someone has won the best of 5
        if user_score == 3 or computer_score == 3:
            print("\n=== GAME OVER ===")
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            else:
                print("The computer wins the game!")
            
            play_again = input("\nPlay again? (yes/no): ").lower().strip()
            if play_again.startswith("y"):
                user_score = 0
                computer_score = 0
                ties = 0
                round_num = 1
            else:
                break
    
    print("\nFinal Score:")
    print(f"You: {user_score}, Computer: {computer_score}, Ties: {ties}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()