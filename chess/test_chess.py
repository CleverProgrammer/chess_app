import unittest
from chess import Piece, Knight


class TestChess(unittest.TestCase):
    def test_knight(self):
        knight1 = Knight('b1')
        moves, captures = knight1.valid_moves()
        self.assertEqual(knight1.color, 'w')
        self.assertTrue('b1' in Piece.occupied_squares)
        self.assertEqual({'a3', 'c3', 'd2'}, moves)
        self.assertEqual(set(), captures)

        # Let's add in another knight.
        knight2 = Knight('d2', 'b')
        self.assertEqual(({'a3', 'c3'}, {'d2'}), knight1.valid_moves())


if __name__ == '__main__':
    unittest.main()
