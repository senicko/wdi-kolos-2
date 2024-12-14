from math import log, floor


def get_factors(n):
    factors = [None for _ in range(floor(log(n, 2)) + 1)]
    factor = 2
    i = 0

    while factor * factor < n:
        if n % factor == 0:
            factors[i] = factor
            i += 1
            while n % factor == 0:
                n //= factor
        factor += 1

    if n > 1:
        factors[i] = n

    return factors


def check_invariant(f1, f2):
    ok = False

    for i in range(len(f1)):
        for j in range(len(f2)):
            if f1[i] == f2[j]:
                ok = not ok

                if not ok:
                    return False

    return ok


def four(T):
    n = len(T)
    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    counter = 0

    for r in range(1, n - 1):
        for c in range(1, n - 1):
            valid = True

            for n1 in range(4):
                n1r, n1c = neighbours[n1]
                n1_factors = get_factors(T[r + n1r][c + n1c])

                for n2 in range(1, 4):
                    n2r, n2c = neighbours[(n1 + n2) % len(neighbours)]
                    n2_factors = get_factors(T[r + n2r][c + n2c])

                    if not check_invariant(n1_factors, n2_factors):
                        valid = False
                        break

                if not valid:
                    break

            if valid:
                counter += 1


print(get_factors(31))
