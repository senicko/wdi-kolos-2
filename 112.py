def shortest_path(T):
    n = len(T)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    moves = [(1, -2), (1, 2), (2, -1), (2, 1)]

    # When we already are in the last row we have to do 0 steps
    # however if the cell is trap, our distance should be inf.
    for i in range(n):
        dp[n - 1][i] = float("inf") if T[n - 1][i] == 1 else 0

    for r in range(n - 2, -1, -1):
        for c in range(n - 1, -1, -1):
            # We assume it won't be possible to reach this cell
            dp[r][c] = float("inf")

            # If it's actually true, continue
            if T[r][c] == 1:
                continue

            # Otherwise find the shortest path from the
            # cell to the last row.
            for mr, mc in moves:
                if mr + r not in range(n) or c + mc not in range(n):
                    continue

                dp[r][c] = min(dp[r][c], dp[r + mr][c + mc] + 1)

    return min(dp[0])


print(
    shortest_path(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1],
        ]
    )
)
