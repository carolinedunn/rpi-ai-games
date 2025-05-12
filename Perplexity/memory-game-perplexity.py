import tkinter as tk
import random
from functools import partial

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("4x4 Animal Matching Game")
        self.buttons = []
        self.first = None
        self.second = None
        self.lock = False
        self.matches_found = 0

        # List of 8 animal names (you can change these if you like)
        animals = ['Dog', 'Cat', 'Mouse', 'Rabbit', 'Fox', 'Bear', 'Panda', 'Koala']
        symbols = animals * 2  # 8 pairs
        random.shuffle(symbols)
        self.symbols = [symbols[i*4:(i+1)*4] for i in range(4)]

        self.create_widgets()

    def create_widgets(self):
        for r in range(4):
            row = []
            for c in range(4):
                btn = tk.Button(self.root, text=" ", width=10, height=3,
                                font=("Arial", 14),
                                command=partial(self.reveal, r, c))
                btn.grid(row=r, column=c, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def reveal(self, r, c):
        if self.lock or self.buttons[r][c]['text'] != " ":
            return

        self.buttons[r][c]['text'] = self.symbols[r][c]
        self.buttons[r][c]['state'] = 'disabled'

        if not self.first:
            self.first = (r, c)
        elif not self.second:
            self.second = (r, c)
            self.root.after(500, self.check_match)

    def check_match(self):
        r1, c1 = self.first
        r2, c2 = self.second
        if self.symbols[r1][c1] == self.symbols[r2][c2]:
            self.matches_found += 1
            if self.matches_found == 8:
                self.show_win_message()
        else:
            self.buttons[r1][c1]['text'] = " "
            self.buttons[r2][c2]['text'] = " "
            self.buttons[r1][c1]['state'] = 'normal'
            self.buttons[r2][c2]['state'] = 'normal'
        self.first = None
        self.second = None

    def show_win_message(self):
        win = tk.Toplevel(self.root)
        win.title("Congratulations!")
        tk.Label(win, text="You matched all the animals!").pack(padx=20, pady=20)
        tk.Button(win, text="Play Again", command=self.restart).pack(pady=10)
        tk.Button(win, text="Quit", command=self.root.quit).pack(pady=5)

    def restart(self):
        for row in self.buttons:
            for btn in row:
                btn.destroy()
        self.buttons = []
        self.first = None
        self.second = None
        self.lock = False
        self.matches_found = 0
        animals = ['Dog', 'Cat', 'Mouse', 'Rabbit', 'Fox', 'Bear', 'Panda', 'Koala']
        symbols = animals * 2
        random.shuffle(symbols)
        self.symbols = [symbols[i*4:(i+1)*4] for i in range(4)]
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
