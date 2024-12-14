from math import inf


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def in_bounds(w, k, n):
    return 0 <= w < n and 0 <= k < n


def solve(t):
    n = len(t)

    def rec(w, k, target_w, target_k, moves):
        if w == target_w and k == target_k:
            return 0

        steps = inf

        for mw, mk in moves:
            tw, tk = w + mw, k + mk
            if not in_bounds(tw, tk, n) or gcd(t[w][k], t[tw][tk]) != 1:
                continue
            steps = min(steps, 1 + rec(tw, tk, target_w, target_k, moves))

        return steps

    a = rec(0, 0, n - 1, n - 1, [(1, 0), (0, 1)])
    b = rec(0, n - 1, n - 1, 0, [(1, 0), (0, -1)])

    if a == b:
        return 0

    return 1 if a < b else 2


T = [
    [1, 1, 1, 4, 4],
    [1, 1, 1, 40, 4],
    [4, 5, 9, 4, 4],
    [1, 1, 1, 4, 1],
    [3, 1, 1, 4, 1],
]

print(
    solve(T),
)
