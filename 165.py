def solve(T):
    n = len(T)

    def rec(a=0, asize=0, b=0, bsize=0, i=0):
        # Base case.
        if i == n:
            # Sprawdzamy czy suma elementow jest taka sama
            # i czy ilosc elementow jest taka sama.
            if a == b and asize == bsize:
                return True

            return False

        return rec(a + T[i], asize + 1, b, bsize, i + 1) or rec(
            a, asize, b + T[i], bsize + 1, i + 1
        )

    return rec()


print(solve([1, 1, 1, 1, 1, 1]))
