import random

def make_board(m=3):

    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i] and all(row[j] != x for row in board) and all(x not in row[j0:j0+m] for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            board[i][j] = None
            return None

    return search()

print(make_board(1))
print(make_board(2))
print(make_board(3))
