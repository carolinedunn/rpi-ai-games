import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Memory Game")
        self.root.resizable(False, False)
        
        # Game parameters
        self.rows = 4
        self.cols = 4
        self.pairs = (self.rows * self.cols) // 2
        
        # Game state
        self.cards = []
        self.flipped = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_active = False
        
        # Animal names and colors for better visibility
        self.animals = [
            ("Dog", "#FFD700"),    # Gold
            ("Cat", "#FF6347"),    # Tomato
            ("Mouse", "#7B68EE"),  # MediumSlateBlue
            ("Rabbit", "#3CB371"), # MediumSeaGreen
            ("Bear", "#CD853F"),   # Peru
            ("Fox", "#FF8C00"),    # DarkOrange
            ("Panda", "#708090"),  # SlateGray
            ("Tiger", "#FF4500"),  # OrangeRed
        ]
        
        # UI elements
        self.card_buttons = []
        self.status_label = tk.Label(root, text="Press New Game to start", font=("Arial", 12))
        self.status_label.grid(row=self.rows, column=0, columnspan=self.cols, pady=10)
        
        self.moves_label = tk.Label(root, text="Moves: 0", font=("Arial", 12))
        self.moves_label.grid(row=self.rows+1, column=0, columnspan=self.cols//2, pady=5)
        
        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game, font=("Arial", 12))
        self.new_game_button.grid(row=self.rows+1, column=self.cols//2, columnspan=self.cols//2, pady=5)
        
        # Initialize the board with empty buttons
        self.create_board()
        
    def create_board(self):
        # Create a frame for the card grid
        card_frame = tk.Frame(self.root)
        card_frame.grid(row=0, column=0, rowspan=self.rows, columnspan=self.cols)
        
        # Create buttons for each card position
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                button = tk.Button(card_frame, text="", width=6, height=3, 
                                  font=("Arial", 10, "bold"),
                                  command=lambda r=row, c=col: self.flip_card(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.card_buttons.append(button_row)
    
    def new_game(self):
        # Reset game state
        self.cards = []
        self.card_colors = []
        self.flipped = []
        self.matched_pairs = 0
        self.moves = 0
        self.game_active = True
        
        # Update labels
        self.moves_label.config(text="Moves: 0")
        self.status_label.config(text="Find matching animal pairs!")
        
        # Use only as many animals as we need pairs
        game_animals = self.animals[:self.pairs]
        
        # Generate card pairs with animals
        animal_names = [animal[0] for animal in game_animals]
        animal_colors = [animal[1] for animal in game_animals]
        
        # Double the lists to create pairs
        all_names = animal_names * 2
        all_colors = animal_colors * 2
        
        # Create a list of indices and shuffle it
        indices = list(range(len(all_names)))
        random.shuffle(indices)
        
        # Reorder the names and colors using the shuffled indices
        self.cards = [all_names[i] for i in indices]
        self.card_colors = [all_colors[i] for i in indices]
        
        # Convert the flat lists to 2D arrays
        self.cards = [self.cards[i:i+self.cols] for i in range(0, len(self.cards), self.cols)]
        self.card_colors = [self.card_colors[i:i+self.cols] for i in range(0, len(self.card_colors), self.cols)]
        
        # Reset all buttons
        for row in range(self.rows):
            for col in range(self.cols):
                self.card_buttons[row][col].config(text="", bg="lightblue", fg="black", state=tk.NORMAL)
    
    def flip_card(self, row, col):
        if not self.game_active or len(self.flipped) >= 2:
            return
        
        # Check if the card is already flipped or matched
        if (row, col) in self.flipped or self.card_buttons[row][col]["bg"] == "lightgreen":
            return
        
        # Show the card
        self.card_buttons[row][col].config(
            text=self.cards[row][col], 
            bg=self.card_colors[row][col],
            fg="white"  # White text for better contrast
        )
        self.flipped.append((row, col))
        
        # If two cards are flipped, check for a match
        if len(self.flipped) == 2:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            
            r1, c1 = self.flipped[0]
            r2, c2 = self.flipped[1]
            
            if self.cards[r1][c1] == self.cards[r2][c2]:
                # Match found
                self.card_buttons[r1][c1].config(bg="lightgreen", fg="black")
                self.card_buttons[r2][c2].config(bg="lightgreen", fg="black")
                self.matched_pairs += 1
                self.flipped = []
                
                # Check if all pairs have been matched
                if self.matched_pairs == self.pairs:
                    self.game_active = False
                    self.status_label.config(text=f"Game Over! You won in {self.moves} moves!")
            else:
                # No match, flip back after a delay
                self.root.after(1000, self.flip_back)
    
    def flip_back(self):
        r1, c1 = self.flipped[0]
        r2, c2 = self.flipped[1]
        
        self.card_buttons[r1][c1].config(text="", bg="lightblue", fg="black")
        self.card_buttons[r2][c2].config(text="", bg="lightblue", fg="black")
        
        self.flipped = []

# Create the main window and start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()