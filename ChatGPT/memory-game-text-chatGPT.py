import tkinter as tk
import random
from functools import partial
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Memory Game - 4x4")
        self.buttons = {}
        self.first = None
        self.second = None
        self.locked = False
        self.matches_found = 0

        self.grid_size = 4
        self.total_pairs = (self.grid_size * self.grid_size) // 2

        # Animal names (8 pairs needed)
        animals = ['Dog', 'Cat', 'Lion', 'Frog', 'Monkey', 'Panda', 'Pig', 'Rabbit']
        animal_pairs = animals * 2
        random.shuffle(animal_pairs)
        self.board = [animal_pairs[i:i+self.grid_size] for i in range(0, len(animal_pairs), self.grid_size)]

        self.create_widgets()

    def create_widgets(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                btn = tk.Button(self.root, text="???", width=10, height=3, font=("Arial", 14),
                                command=partial(self.reveal_card, row, col))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[(row, col)] = btn

    def reveal_card(self, row, col):
        if self.locked or self.buttons[(row, col)]['state'] == 'disabled':
            return

        btn = self.buttons[(row, col)]
        btn.config(text=self.board[row][col], state='disabled')

        if not self.first:
            self.first = (row, col)
        elif not self.second:
            self.second = (row, col)
            self.locked = True
            self.root.after(1000, self.check_match)

    def check_match(self):
        r1, c1 = self.first
        r2, c2 = self.second

        if self.board[r1][c1] != self.board[r2][c2]:
            self.buttons[(r1, c1)].config(text="???", state='normal')
            self.buttons[(r2, c2)].config(text="???", state='normal')
        else:
            self.matches_found += 1
            if self.matches_found == self.total_pairs:
                messagebox.showinfo("Animal Memory Game", "🎉 You matched all the animals!")

        self.first = None
        self.second = None
        self.locked = False

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
