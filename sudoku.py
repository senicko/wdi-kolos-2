def digit_ok(board, at_r, at_c, d):
    for r in range(3):
        for c in range(3):
            if board[r + (at_r // 3) * 3][c + (at_c // 3) * 3] == d:
                return False

    for i in range(9):
        if board[at_r][i] == d or board[i][at_c] == d:
            return False

    return True


def sudoku_solver(board, i=0):
    if i == 9 * 9:
        return True

    r, c = i // 9, i % 9

    if board[r][c] != 0:
        return sudoku_solver(board, i + 1)

    for v in range(1, 10):
        if not digit_ok(board, r, c, v):
            continue

        board[r][c] = v
        if sudoku_solver(board, i + 1):
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
