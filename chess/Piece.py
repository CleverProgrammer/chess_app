"""
Chess pieces file.
"""
import pprint

pp = pprint.PrettyPrinter()
BOARD = [['{}{}'.format(file_, rank) for file_ in 'abcdefgh'] for rank in range(1, 9)]
coordinate_map = {key: (row_index, col_index)
                  for row_index, row in enumerate(BOARD) for col_index, key in enumerate(row)}

print(coordinate_map)


class Piece:
    piece_count = 0
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
        Piece.piece_count += 1

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


    def valid_moves(self):
        row, col = coordinate_map[self.position]
        print(BOARD[row + 2][col + 1])
        # try:
        # except IndexError:
            # print("Your move is off the board")

    def move(self, square):
        row, col = coordinate_map[square]
        BOARD[row][col] = 'N'

# file_rank_to_indices

knight = Knight('w', 'g1')
knight2 = Knight('w', 'b1')
print(knight)
print(knight.file, knight.rank)
print(knight2)

print(Piece.piece_count)
print(Knight.KNIGHTS)

pp.pprint(BOARD)
# print(BOARD[0].index('g1'))
print(knight.valid_moves())
knight.move('f3')
knight.move('g5')
pprint.pprint(BOARD[::-1])
# print(BOARD[row][col])
