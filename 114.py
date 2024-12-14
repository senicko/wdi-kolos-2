def chess(T):
    print(*T, sep="\n")

    n = len(T)

    row_sums = [0 for _ in range(n)]
    col_sums = [0 for _ in range(n)]

    for r in range(n):
        for c in range(n):
            row_sums[r] += T[r][c]
            col_sums[c] += T[r][c]

    def get_sum(r, c):
        return row_sums[r] + col_sums[c] - 2 * T[r][c]

    max_sum = 0
    ans = None

    for r1 in range(n * n):
        r1_row = r1 // n
        r1_col = r1 % n

        for r2 in range(r1 + 1, n * n):
            r2_row = r2 // n
            r2_col = r2 % n

            if r1_row == r2_row or r2_col == r1_col:
                continue

            current_sum = get_sum(r1_row, r1_col) + get_sum(r2_row, r2_col)

            if current_sum > max_sum:
                max_sum = current_sum
                ans = (r1_row, r1_col, r2_row, r2_col)

    return ans


print(chess([[4, 0, 2], [3, 0, 0], [6, 5, 3]]))
