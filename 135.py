from math import inf


def in_bounds(r, c, n):
    return r in range(n) and c in range(n)


# da sie tez rekurencja, ale to jest OP
def shortest_path(T, k):
    n = len(T)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[n - 1][i] = T[n - 1][i]

    for r in range(n - 2, -1, -1):
        for c in range(n - 1, -1, -1):
            minimum = inf
            moves = [(1, 0), (1, 1), (1, -1)]

            for mr, mc in moves:
                if not in_bounds(r + mr, c + mc, n):
                    continue

                minimum = min(minimum, dp[r + mr][c + mc])

            dp[r][c] = T[r][c] + minimum

    return dp[0][k]


print(
    shortest_path(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        2,
    )
)
