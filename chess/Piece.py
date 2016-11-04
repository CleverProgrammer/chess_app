"""
Chess pieces file.
"""
import pprint

pp = pprint.PrettyPrinter()
BOARD = [['{}{}'.format(file_, rank) for file_ in 'abcdefgh'] for rank in range(1, 9)]
square_to_indices_map = {key: (row_index, col_index)
                         for row_index, row in enumerate(BOARD) for col_index, key in enumerate(row)}

print(square_to_indices_map)


class Piece:
    occupied_squares = []
    piece_count = 0
    PIECE_VALUES = {
        'pawn'  : 1,
        'knight': 3,
        'bishop': 3,
        'rook'  : 5,
        'queen' : 9,
        'king'  : 10000
    }

    def __init__(self, name, color, square=None):
        self.name = name
        self.color = color
        self.square = square
        self.value = self.PIECE_VALUES[self.name]
        Piece.piece_count += 1

    def valid_moves(self):
        raise NotImplementedError

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.value, self.color, self.square)


class Knight(Piece):
    KNIGHTS = 0

    def __init__(self, color, square):
        super(Knight, self).__init__('knight', color, square)
        Knight.KNIGHTS += 1
        self.file, self.rank = square[0], square[1]

    def valid_moves(self):
        row, col = square_to_indices_map[self.square]
        try:
            one = BOARD[abs(row + 2)][abs(col + 1)]
        except IndexError:
            one = None

        try:
            two = BOARD[abs(row + 2)][abs(col - 1)]
        except IndexError:
            two = None

        try:
            three = BOARD[abs(row + 1)][abs(col + 2)]
        except IndexError:
            three = None

        try:
            four = BOARD[abs(row + 1)][abs(col - 2)]
        except IndexError:
            four = None

        try:
            five = BOARD[abs(row - 1)][abs(col - 2)]
        except IndexError:
            five = None

        try:
            six = BOARD[abs(row - 1)][abs(col + 2)]
        except IndexError:
            six = None

        try:
            seven = BOARD[abs(row - 2)][abs(col - 1)]
        except IndexError:
            seven = None

        try:
            eight = BOARD[abs(row - 2)][abs(col + 1)]
        except IndexError:
            eight = None

        knight_moves = {one, two, three, four, five, six, seven, eight}
        allowed_on_board_moves = {move for move in knight_moves if move is not None}
        return allowed_on_board_moves

    def move(self, square):
        row, col = square_to_indices_map[square]
        BOARD[row][col] = 'N'


# file_rank_to_indices

knight = Knight('w', 'e4')
# knight2 = Knight('w', 'b1')
print(knight)
print(knight.file, knight.rank)
# print(knight2)

print(Piece.piece_count)
print(Knight.KNIGHTS)

pp.pprint(BOARD)
# print(BOARD[0].index('g1'))
print(knight.valid_moves())
# knight.move('f3')
# knight.move('g5')
# print(BOARD[row][col])
row, col = square_to_indices_map['e4']
# BOARD[row][col] = 'N'
pprint.pprint(BOARD[::-1])
pprint.pprint(knight.valid_moves())
print(knight.value)
