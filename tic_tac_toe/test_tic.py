import unittest 
import numpy as np 

from tic import make_move, winner_check

class TestTic(unittest.TestCase):
    def test_make_move(self):
        #here checking whether the move is valid or not by giving the edge cases
        #if the move is valid, it must be defined within the board 
        board = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
        self.assertTrue(make_move(board,0, 0, 'O'))
        self.assertFalse(make_move(board, 0, 0 , 'X'))

    def test_winner_check(self):
        board = np.array ([['X','O','X'], ['X','O','X'],['X','O','X']])
        self.assertTrue(winner_check(board, 'X'))
        self.assertFalse(winner_check(board, 'O'))

if __name__ == "__main__":
    unittest.main()


