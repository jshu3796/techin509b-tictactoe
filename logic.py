# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for a in range(len(board)):
        if board[0][a] == board[1][a] == board[2][a] and board[0][a] is not None:
            return board[0][a]

    if all(board[i][i] == board[0][0] and board[i][i] is not None for i in range(3)) or all(
            board[i][2 - i] == board[0][2] and board[i][2 - i] is not None for i in range(3)):
        return board[1][1]

    if all(cell is not None for row in board for cell in row):
        return None

    return None


def other_player(player):
    return "O" if player == "X" else "X"
