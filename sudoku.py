def digit_ok(board, at_r, at_c, d):
    # Przechodzimy przez wartosci aktualnego kwadratu
    for r in range(3):
        for c in range(3):
            # Jezeli w kwadracie jest d, to nie
            # mozemy go kolejny raz uzyc.
            if board[r + (at_r // 3) * 3][c + (at_c // 3) * 3] == d:
                return False

    # Sprawdzamy czy w aktualnym wierszu lub
    # kolumnie jest juz uzyte d.
    for i in range(9):
        if board[at_r][i] == d or board[i][at_c] == d:
            return False

    return True


def sudoku_solver(board, r=0, c=0):
    if r == 9:
        return True

    # Funkcja pomocnicza do okreslania nastepnej pozycji w sudoku
    def next_position(r, c):
        if c < 8:
            return r, c + 1
        else:
            return r + 1, 0

    next_r, next_c = next_position(r, c)

    # Jezeli aktualna komorka ma juz jakas liczbe,
    # to ja skipujemy
    if board[r][c] != 0:
        return sudoku_solver(board, next_r, next_c)

    # Dla kazdej mozliwej wartosci komorki
    for v in range(1, 10):
        if not digit_ok(board, r, c, v):
            continue

        board[r][c] = v
        if sudoku_solver(board, next_r, next_c):
            return True
        board[r][c] = 0

    return False


board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

sudoku_solver(board)

print(*board, sep="\n")
