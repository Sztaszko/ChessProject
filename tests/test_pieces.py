import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chess.pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class TestPiece(unittest.TestCase):
    def test_piece_constructor_valid_color(self):
        piece = Piece('white')
        self.assertEqual(piece.color, 'white')

    def test_piece_constructor_invalid_color(self):
        with self.assertRaises(ValueError):
            Piece('invalid_color')

    def test_piece_validate_move_abstract_method(self):
        piece = Piece('white')
        with self.assertRaises(NotImplementedError):
            piece.validate_move((0, 0), (1, 1))

    def test_piece_get_movement_path_abstract_method(self):
        piece = Piece('white')
        with self.assertRaises(NotImplementedError):
            piece.get_movement_path((0, 0), (1, 1))

class TestPawn(unittest.TestCase):
    def test_pawn_validate_move_white_valid(self):
        pawn = Pawn('white')
        self.assertTrue(pawn.validate_move((1, 1), (2, 1)))  # Valid move

    def test_pawn_validate_move_white_invalid(self):
        pawn = Pawn('white')
        self.assertFalse(pawn.validate_move((1, 1), (3, 1)))  # Invalid move

    def test_pawn_validate_move_black_valid(self):
        pawn = Pawn('black')
        self.assertTrue(pawn.validate_move((6, 1), (5, 1)))  # Valid move

    def test_pawn_validate_move_black_invalid(self):
        pawn = Pawn('black')
        self.assertFalse(pawn.validate_move((6, 1), (4, 1)))  # Invalid move

    def test_pawn_get_movement_path(self):
        pawn = Pawn('white')
        self.assertEqual(pawn.get_movement_path((1, 1), (3, 1)), [])  # Empty list

class TestRook(unittest.TestCase):
    def test_rook_validate_move_valid(self):
        rook = Rook('white')
        self.assertTrue(rook.validate_move((0, 0), (4, 0)))  # Valid move

    def test_rook_validate_move_invalid(self):
        rook = Rook('white')
        self.assertFalse(rook.validate_move((0, 0), (3, 2)))  # Invalid move

    def test_rook_get_movement_path(self):
        rook = Rook('white')
        self.assertEqual(rook.get_movement_path((0, 0), (4, 0)), [(1, 0), (2, 0), (3, 0)])  # Expected movement path

# Add similar tests for other piece classes

if __name__ == '__main__':
    unittest.main()