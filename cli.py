# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner
a="O"

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        for line in board:
            print(line)
        # TODO: Input a move from the player.
        movement=input(f"plz input 'X,Y',no more than 2 and no less the 0. It's {a}'s turn")
        X,Y=movement.split(',')
        X=int(X)
        Y=int(Y)
        # TODO: Update the board.
        board[X][Y]=a
        # TODO: Update who's turn it is.
        if a=="O":
            a="X"
        elif a=="X":
            a="O"
        winner = get_winner(board)  # FIXME
