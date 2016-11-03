"""
Chess pieces file.
"""
import pprint
import numpy

pp = pprint.PrettyPrinter()
BOARD = [['{}{}'.format(file_, rank) for file_ in 'abcdefgh'] for rank in range(1, 9)]



class Piece:
    PIECES = 0
    PIECE_VALUES = {
        'pawn'  : 1,
        'knight': 3,
        'bishop': 3,
        'rook'  : 5,
        'queen' : 9,
        'king'  : 10000
    }

    def __init__(self, name, value, color, position=None):
        self.name = name
        self.value = value
        self.color = color
        self.position = position
        Piece.PIECES += 1

    def valid_moves(self):
        raise NotImplementedError

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.value, self.color, self.position)


class Knight(Piece):
    KNIGHTS = 0

    def __init__(self, color, position):
        super(Knight, self).__init__('knight', self.PIECE_VALUES['knight'], color, position)
        Knight.KNIGHTS += 1
        self.file, self.rank = position[0], position[1]

    # def valid_moves(self):


#file_rank_to_indices

knight = Knight('w', 'g1')
knight2 = Knight('w', 'b1')
print(knight)
print(knight.file, knight.rank)
print(knight2)

print(Piece.PIECES)
print(Knight.KNIGHTS)

pp.pprint(BOARD)
print(BOARD[0].index('g1'))
# print(BOARD[row][col])
