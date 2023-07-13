import unittest
import Tic_Tac_Toe


# clear board
def clear_board():
    for i in range(Tic_Tac_Toe.ROWS):
        for j in range(Tic_Tac_Toe.COLS):
            Tic_Tac_Toe.board[i][j] = Tic_Tac_Toe.EMPTY


# placing the current value in forward diagonal
def forward_diagonal_input(current):
    Tic_Tac_Toe.board[0][0] = current
    Tic_Tac_Toe.board[1][1] = current
    Tic_Tac_Toe.board[2][2] = current


# placing the current value in backward diagonal
def backward_diagonal_input(current):
    Tic_Tac_Toe.board[0][2] = current
    Tic_Tac_Toe.board[1][1] = current
    Tic_Tac_Toe.board[2][0] = current


# placing the current value in row
def row_input(row, current):
    Tic_Tac_Toe.board[row][0] = current
    Tic_Tac_Toe.board[row][1] = current
    Tic_Tac_Toe.board[row][2] = current


# placing the current value in column
def col_input(col, current):
    Tic_Tac_Toe.board[0][col] = current
    Tic_Tac_Toe.board[1][col] = current
    Tic_Tac_Toe.board[2][col] = current


# Tic_Tac_Toe test class
class TestTicTacToe(unittest.TestCase):
    # Testing moves
    def testIsValid(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 1, 1))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 2, 1))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(5, 1, 1))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(4, 4, 1))
        clear_board()
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 1, 2))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 0, 2))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(4, 1, 2))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1, 4, 2))
        clear_board()

    # Testing winning scenarios
    def testHasWon(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        # check CIRCLE diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        # check CROSS column
        col_input(1, Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        col_input(2, Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        # check CIRCLE column
        clear_board()
        col_input(1, Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        col_input(2, Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        # check CROSS row
        row_input(1, Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        clear_board()
        row_input(2, Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 1))
        # check CIRCLE row
        clear_board()
        row_input(1, Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))
        clear_board()
        row_input(2, Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 1, 1))

    def testValidate(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        # check CIRCLE diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()

    def testBackDiagonal(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        # check CIRCLE diagonals:
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        backward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()

    def testForwardDiagonal(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS diagonals:
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CROSS))
        clear_board()
        # check CIRCLE diagonals:
        forward_diagonal_input(Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()
        forward_diagonal_input(Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CIRCLE))
        clear_board()

    def testCol(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS column
        col_input(1, Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(1, Tic_Tac_Toe.CROSS))
        clear_board()
        col_input(2, Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(1, Tic_Tac_Toe.CROSS))
        # check CIRCLE column
        clear_board()
        col_input(1, Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(1, Tic_Tac_Toe.CIRCLE))
        clear_board()
        col_input(2, Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(1, Tic_Tac_Toe.CIRCLE))

    def testRow(self):
        Tic_Tac_Toe.init_game()
        clear_board()
        # check CROSS row
        row_input(1, Tic_Tac_Toe.CROSS)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(1, Tic_Tac_Toe.CROSS))
        clear_board()
        row_input(2, Tic_Tac_Toe.CROSS)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_row(1, Tic_Tac_Toe.CROSS))
        # check CIRCLE row
        clear_board()
        row_input(1, Tic_Tac_Toe.CIRCLE)
        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(1, Tic_Tac_Toe.CIRCLE))
        clear_board()
        row_input(2, Tic_Tac_Toe.CIRCLE)
        self.assertFalse(Tic_Tac_Toe.validate_3_in_row(1, Tic_Tac_Toe.CIRCLE))


# exe test
if __name__ == '__main__':
    unittest.main()
