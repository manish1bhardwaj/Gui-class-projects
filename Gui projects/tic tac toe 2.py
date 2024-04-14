import tkinter as tk
from tkinter import messagebox as mb
root = tk.Tk()
root.title("Tic Tac Toe")
cp = "X"
board = [" " for _ in range(9)]
def move(row, col):
     global cp
     global board
     if board[row * 3 + col] == " ":
         board[row * 3 + col] = cp
         buttons[row * 3 + col].config(text=cp)
         if winner(cp):
             mb.showinfo("Winner!", f"Player {cp} wins!")
             reset()
         elif " " not in board:
             mb.showinfo("Draw!", "It's a draw!")
             reset()
         else:
             cp = "O" if cp == "X" else "X"
def winner(player):
     combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
                             (0, 4, 8), (2, 4, 6)]
     for c in combinations:
         if board[c[0]] == board[c[1]] == board[c[2]] == player:
             return True
     return False
def reset():
     global cp
     global board
     cp = "X"
     board = [" " for _ in range(9)]
     for button in buttons:
         button.config(text="")
buttons = []
for i in range(3):
     for j in range(3):
         button = tk.Button(root, text="",font="bold", padx=40, pady=40,command=lambda row=i, col=j: move(row, col))
         button.grid(row=i, column=j)
         buttons.append(button)
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=3, column=0, columnspan=3)
root.mainloop()