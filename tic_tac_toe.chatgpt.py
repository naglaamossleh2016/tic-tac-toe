import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = random.choice(['X', 'O'])
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.score = {'X': 0, 'O': 0}
        self.winning_cells = set()

        # Create buttons
        self.buttons = [[tk.Button(root, text='', font=('normal', 20), width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j)) for j in range(3)] for i in range(3)]

        # Place buttons on the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

        # Label to display current player
        self.current_player_label = tk.Label(root, text=f"Current Player: {self.current_player}", font=('normal', 12))
        self.current_player_label.grid(row=3, column=0, columnspan=3)

        # Label to display winner or tie
        self.result_label = tk.Label(root, text="", font=('normal', 12, 'bold'))
        self.result_label.grid(row=4, column=0, columnspan=3)

        # Label to display score
        self.score_label = tk.Label(root, text=f"Score: X - {self.score['X']}  O - {self.score['O']}", font=('normal', 12))
        self.score_label.grid(row=5, column=0, columnspan=3)

        # Restart button
        restart_button = tk.Button(root, text="Restart", font=('normal', 12), command=self.reset_game)
        restart_button.grid(row=6, column=0, columnspan=3)

    def on_click(self, i, j):
        if self.board[i][j] == '' and not self.check_winner():
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)

            if self.check_winner():
                self.highlight_winning_cells()
                self.result_label.config(text=f"Player {self.current_player} wins!", fg='green')
                self.score[self.current_player] += 1
                self.update_score()
            elif all(self.board[i][j] != '' for i in range(3) for j in range(3)):
                self.result_label.config(text="It's a tie!", fg='orange')
                self.highlight_tie_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.current_player_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                self.winning_cells = {(i, 0), (i, 1), (i, 2)}
                return True  # Row
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                self.winning_cells = {(0, i), (1, i), (2, i)}
                return True  # Column

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            self.winning_cells = {(0, 0), (1, 1), (2, 2)}
            return True  # Diagonal from top-left to bottom-right
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            self.winning_cells = {(0, 2), (1, 1), (2, 0)}
            return True  # Diagonal from top-right to bottom-left

        return False

    def highlight_winning_cells(self):
        for i, row in enumerate(self.buttons):
            for j, button in enumerate(row):
                if (i, j) in self.winning_cells:
                    button.config(bg='lightgreen')

    def highlight_tie_board(self):
        for row in self.buttons:
            for button in row:
                button.config(bg='orange')

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='', bg='SystemButtonFace')

        self.current_player = random.choice(['X', 'O'])
        self.current_player_label.config(text=f"Current Player: {self.current_player}")
        self.result_label.config(text="")
        self.update_score()
        self.winning_cells = set()

    def update_score(self):
        self.score_label.config(text=f"Score: X - {self.score['X']}  O - {self.score['O']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
