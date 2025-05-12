import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Animal Memory Game")

        self.rows = 4
        self.cols = 4
        self.grid_size = self.rows * self.cols
        self.animals = self._generate_animals()
        self.board = [None] * self.grid_size
        self.buttons = []
        self.flipped = []
        self.matches = 0
        self.attempts = 0

        self._create_board()
        self._shuffle_board()
        self._create_widgets()

    def _generate_animals(self):
        animal_list = ["Dog", "Cat", "Bear", "Rabbit", "Lion", "Tiger", "Elephant", "Panda"]
        # Create pairs of animals
        animal_pairs = animal_list * 2
        return animal_pairs

    def _create_board(self):
        # Initialize the board with animals
        self.board = self.animals[:] # Create a copy
        random.shuffle(self.board)

    def _shuffle_board(self):
        # Shuffle the board again in case initialization didn't fully randomize
        random.shuffle(self.board)

    def _create_widgets(self):
        self.attempt_label = tk.Label(self.master, text="Attempts: 0")
        self.attempt_label.grid(row=self.rows, column=0, columnspan=self.cols, pady=10)

        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                button = tk.Button(
                    self.master,
                    text="",
                    width=8,  # Adjust width for text
                    height=3,
                    font=("Arial", 12),
                    command=lambda row=r, col=c: self._button_click(row, col),
                )
                button.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def _button_click(self, row, col):
        index = row * self.cols + col
        if index in [f[0] for f in self.flipped] or self.buttons[row][col]["state"] == tk.DISABLED:
            return

        self.buttons[row][col]["text"] = self.board[index]
        self.flipped.append((index, self.buttons[row][col]))

        if len(self.flipped) == 2:
            self.attempts += 1
            self.attempt_label.config(text=f"Attempts: {self.attempts}")
            self.master.after(1000, self._check_match)

    def _check_match(self):
        if len(self.flipped) != 2:
            return

        index1, button1 = self.flipped[0]
        index2, button2 = self.flipped[1]

        if self.board[index1] == self.board[index2]:
            button1.config(state=tk.DISABLED)
            button2.config(state=tk.DISABLED)
            self.matches += 1
            if self.matches == self.grid_size // 2:
                messagebox.showinfo("Congratulations!", f"You won in {self.attempts} attempts!")
        else:
            button1["text"] = ""
            button2["text"] = ""

        self.flipped = []

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()