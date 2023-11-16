import unittest
from unittest.mock import patch
from io import StringIO
from logic import Game, Board, Human, Bot, make_empty_board, get_winner, other_player

class TicTacToeTests(unittest.TestCase):

    def test_make_empty_board(self):
        """Test if make_empty_board returns an empty 3x3 board."""
        board = make_empty_board()
        self.assertEqual(len(board), 3)
        self.assertEqual(len(board[0]), 3)
        self.assertEqual(board[0][0], None)

    def test_get_winner(self):
        """Test the get_winner function for various winning scenarios and draws."""
        # Test for a winning row
        board1 = [['X', 'X', 'X'],
                  [' ', 'O', ' '],
                  ['O', ' ', 'O']]
        self.assertEqual(get_winner(board1), 'X')

        # Test for a draw
        board2 = [['O', 'X', 'O'],
                  ['O', 'X', 'X'],
                  ['X', 'O', 'O']]
        self.assertIsNone(get_winner(board2))

        # Add more scenarios in the documentation as needed

    def test_other_player(self):
        """Test if other_player correctly switches between 'X' and 'O'."""
        player_x = 'X'
        player_o = 'O'
        self.assertEqual(other_player(player_x), player_o)
        self.assertEqual(other_player(player_o), player_x)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['0,0', '0,1', '1,1', '2,0', '2,1', 'multi'])
    class TicTacToeTests(unittest.TestCase):
     @patch('builtins.input', side_effect=['0,0', '1,1', '2,2', 'exit'])
     def test_game_run_single_player(self, mock_input):
        game = Game(Human('X'), Bot('O'))
        game.run()

    @patch('builtins.input', side_effect=['0,0', '1,1', '2,2', 'exit'])
    def test_game_run_multi_player(self, mock_input):
        game = Game(Human('X'), Human('O'))
        game.run()
    def test_board_make_move(self):
        """Test the make_move method of the Board class."""
        # The make_move method is tested for making a valid move and an invalid move.
        board = Board()
        self.assertTrue(board.make_move(0, 0, 'X'))
        self.assertFalse(board.make_move(0, 0, 'O'))
        # Add more assertions as needed

if __name__ == '__main__':
    unittest.main()
