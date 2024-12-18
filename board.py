import random

class Board:
    def __init__(self, size):
        self.rows = size[0]
        self.columns = size[1]
        self.board = [['~' for _ in range(self.columns)] for _ in range(self.rows)]

    def print_board(self, reveal_ships):
        result = '  ' + ' '.join([str(i+1) for i in range(self.columns)]) + '\n'
        for i in range(self.rows):
            result += chr(i+65) + ' '  # Row letters (A, B, C, ...)
            for j in range(self.columns):
                if reveal_ships:
                    result += self.board[i][j] + ' '
                else:
                    result += '~ '  # Use ~ to hide the ships
            result += '\n'
        return result

    def place_ship(self, ship):
        while True:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.columns - ship.length)
                if all(self.board[row][col+i] == '~' for i in range(ship.length)):
                    for i in range(ship.length):
                        self.board[row][col+i] = 'S'
                        ship.coordinates.append([row, col+i])
                    break
            else:
                row = random.randint(0, self.rows - ship.length)
                col = random.randint(0, self.columns - 1)
                if all(self.board[row+i][col] == '~' for i in range(ship.length)):
                    for i in range(ship.length):
                        self.board[row+i][col] = 'S'
                        ship.coordinates.append([row+i, col])
                    break

    def update_board(self, shot):
        row, col = shot
        if self.board[row][col] == 'S':
            self.board[row][col] = 'X'
            return "hit"
        else:
            self.board[row][col] = 'O'
            return "miss"
