# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import logging

class Game:
    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO

    def run(self):
        current_player = self._playerX
        while not self._game_over():
            self._board.print_board()
            move = current_player.get_move(self._board.get_board())
            row, col = move
            if self._board.make_move(row, col, current_player.get_symbol()):
                logging.info(f"{current_player.get_symbol()} made a move at ({row}, {col})")
                current_player = self._playerO if current_player == self._playerX else self._playerX
            else:
                print("Invalid move. Cell already occupied. Try again.")
        self._board.print_board()
        winner = get_winner(self._board.get_board())
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")
            
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
    def _game_over(self):
        return get_winner(self._board.get_board()) or all(
            self._board.get_board()[i][j] != '' for i in range(3) for j in range(3)
        )

class Board:
    def __init__(self):
        self._board = [['' for _ in range(3)] for _ in range(3)]

    def get_board(self):
        return self._board

    def make_move(self, row, col, player):
        if self._board[row][col] == '':
            self._board[row][col] = player
            return True
        else:
            return False

    def print_board(self):
        print("Current Board:")
        print("-" * 9)
        for row in self._board:
            print(" | ".join(cell if cell != '' else " " for cell in row))
            print("-" * 9)

class Player:
    def __init__(self, symbol):
        self._symbol = symbol

    def get_move(self, board):
        pass

    def get_symbol(self):
        return self._symbol

class Human(Player):
    def get_move(self, board):
        try:
            move = input(f"Please input 'row,col' (0 <= row, col <= 2). It's {self._symbol}'s turn: ")
            row, col = map(int, move.split(','))
            return row, col
        except (ValueError, IndexError):
            print("Invalid input format. Please use 'row,col'. Try again.")
            return self.get_move(board)

class Bot(Player):
    def get_move(self, board):
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
        return random.choice(available_moves)



if __name__ == '__main__':
    player_mode = input('Enter "single" for single player or "multi" for two players: ')
    
    if player_mode == 'single':
        game = Game(Human('X'), Bot('O'))
    elif player_mode == 'multi':
        game = Game(Human('X'), Human('O'))
    else:
        print("Invalid input. Please enter 'single' or 'multi'.")
        exit(1)

    game.run()





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
