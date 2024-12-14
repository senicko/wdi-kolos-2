def solve(T, product):
    n = len(T)

    moves = [(1, -2), (1, 2), (2, -1), (2, 1)]
    counter = 0

    for r in range(n):
        for c in range(n):
            if product % T[r][c] != 0:
                continue

            for mr, mc in moves:
                # Check bounds.
                if r + mr not in range(n) or c + mc not in range(n):
                    continue

                # Check product.
                if T[r + mr][c + mc] * T[r][c] == product:
                    counter += 1

    return counter


print(
    solve(
        [
            [1, 1, 1, 2, 1],
            [1, 2, 1, 1, 1],
            [1, 1, 1, 1, 5],
            [1, 1, 5, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        10,
    )
)
