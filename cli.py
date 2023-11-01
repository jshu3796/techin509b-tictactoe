# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logging
from logic import make_empty_board, get_winner

logging.basicConfig(
    filename='logs/infos.log',
    level=logging.INFO
)

def print_board(board):
    print("Current Board:")
    print("-" * 5)
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 5)

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = "O"

    while winner is None:
        print_board(board)

        movement = input(f"Please input 'row,col' (0 <= row, col <= 2). It's {current_player}'s turn: ")
        try:
            row, col = map(int, movement.split(','))

            if board[row][col] is None:
                board[row][col] = current_player
            else:
                print("Invalid move. Cell already occupied. Try again.")
                continue

            logging.info(f"Board state: {board}")
            logging.info(f"{current_player} made a move at ({row}, {col})")

            current_player = "X" if current_player == "O" else "O"
            winner = get_winner(board)

        except ValueError:
            print("Invalid input format. Please use 'row,col'. Try again.")

    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
