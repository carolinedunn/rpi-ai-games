import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Animal Memory Game")

# Define grid size
ROWS, COLS = 4, 4
animals = [
    "Dog", "Dog", "Cat", "Cat", "Rabbit", "Rabbit", "Frog", "Frog",
    "Monkey", "Monkey", "Fox", "Fox", "Wolf", "Wolf", "Bear", "Bear"
]  # Matching pairs
random.shuffle(animals)

# Track revealed cards
revealed = [[None] * COLS for _ in range(ROWS)]
selected = []

# Functions
def reveal_card(row, col):
    global selected
    if revealed[row][col] is None and len(selected) < 2:
        buttons[row][col].config(text=animals[row * COLS + col])
        selected.append((row, col))

    if len(selected) == 2:
        root.after(1000, check_match)

def check_match():
    global selected
    r1, c1 = selected[0]
    r2, c2 = selected[1]
    
    if animals[r1 * COLS + c1] == animals[r2 * COLS + c2]:  # Match found
        revealed[r1][c1] = revealed[r2][c2] = animals[r1 * COLS + c1]
    else:
        buttons[r1][c1].config(text="")
        buttons[r2][c2].config(text="")
    
    selected = []

# Create buttons
buttons = [[None] * COLS for _ in range(ROWS)]
for r in range(ROWS):
    for c in range(COLS):
        btn = tk.Button(root, text="", width=10, height=3, command=lambda r=r, c=c: reveal_card(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

# Start the game loop
root.mainloop()
