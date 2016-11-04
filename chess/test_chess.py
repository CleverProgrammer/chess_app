import unittest
from chess import Piece
from chess import Knight


class TestFifteen(unittest.TestCase):
    def test_knight(self):
        knight1 = Knight('b1')
        self.assertEqual(knight1.color, 'w')
        # self.assertEqual(fifteen.lower_row_invariant(2, 1), True)


if __name__ == '__main__':
    unittest.main()
