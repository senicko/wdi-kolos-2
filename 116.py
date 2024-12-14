from math import inf


def race(T):
    n = len(T)

    dp1 = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp1[n - 1][i] = T[n - 1][i]

    for r in range(n-1, -1, -1):
        for c in range(n-1, -1, -1):
            for mr, mc in [(1, 0), (0, 1)]:
                dp[]
