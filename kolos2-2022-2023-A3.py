def longest_path(N, L):
    visited = [[False for _ in range(N)] for _ in range(N)]
    for pawn in L:
        visited[pawn[0]][pawn[1]] = True
    visited[0][0] = True

    moves = [(1, 0), (-1, 0), (0, 1)]

    def is_valid_move(r, c, n):
        return 0 <= r < n and 0 <= c < n and not visited[r][c]

    def rec(r=0, c=0, steps=0):
        if r == N - 1 and c == N - 1:
            return steps

        longest = 0

        for move in moves:
            tr = r + move[0]
            tc = c + move[1]

            if not is_valid_move(tr, tc, N):
                continue

            visited[tr][tc] = True
            longest = max(longest, rec(tr, tc, steps + 1))
            visited[tr][tc] = False

        return longest

    return rec()


N = 5
L = [
    (0, 1),
]

print(longest_path(N, L))
