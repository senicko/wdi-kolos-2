# is_fib sprawdza czy x i y sa podciagiem ciagu fibonacciego.
def is_fib(x, y):
    a = 1
    b = 1

    while a <= x:
        if a == x and b == y:
            return True
        a, b = b, a + b

    return False


# in_bounds sprawdza czy pozycja jest wewnatrz tablicy NxN.
def in_bounds(r, c, n):
    return r in range(n) and c in range(n)


def find(T):
    n = len(T)

    # funkcja pomocnicza uogolniajaca sprawdzanie warunku
    # w dowolnym kierunku
    def check_direction(r, c, direction):
        dr, dc = direction

        # Jezeli nie mozemy wykonac ruchu to koniec
        if not in_bounds(r + dr, c + dc, n):
            return 0

        # Jezeli dwa elementy w tym kierunku tworza podciag ciagu fibonacciego
        if is_fib(T[r][c], T[r + dr][c + dc]):
            seq = 2
            a = (r, c)
            b = (r + dr, c + dc)

            # Zliczamy maksymalny podciag fibonacciego w tym kierunku
            while (
                in_bounds(b[0] + dr, b[1] + dc, n)
                and T[b[0] + dr][b[1] + dc] == T[a[0]][a[1]] + T[b[0]][b[1]]
            ):
                a, b = b, (b[0] + dr, b[1] + dc)
                seq += 1

            return seq

        return 0

    maximum = 0

    for r in range(n):
        for c in range(n):
            # Znajdujemy najdluzszy podciag fibonacciego zaczynajacy sie
            # w punkcie [r][c]
            result = max(
                [
                    check_direction(r, c, (1, 0)),
                    check_direction(r, c, (-1, 0)),
                    check_direction(r, c, (0, 1)),
                    check_direction(r, c, (0, -1)),
                ]
            )

            # Aktualizujemy ostateczne znalezione maksimum
            # (z innego punktu mozemy znalezc dluzszy podciag)
            maximum = max(maximum, result)

    return maximum if maximum > 2 else 0


t = [
    [1, 8, 1, 1, 1, 1],
    [1, 5, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 1],
    [1, 2, 1, 5, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

print(find(t))
