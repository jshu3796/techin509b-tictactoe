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
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for row in board:
        if row[0]==row[1]==row[2]=='X':
            return 'X'
        elif row[0]==row[1]==row[2]=='O':
            return 'O'

    for a in range(len(board)):
        if board[0][a]==board[1][a]==board[2][a] == 'X':
            return 'X'
        elif board[0][a]==board[1][a]==board[2][a] == 'O':
            return 'O'

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    if all(cell != '' for row in board for cell in row):
        return  None

    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O"  # FIXME
