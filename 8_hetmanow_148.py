def queens():
    # Nie wiem czy mozna set'a, ale tak jest najlepiej.
    # Jak nie to mozna te wartosci trzymac w tablicy
    # i liniowo sprawdzac czy maja jakas wartosc.
    diag_asc = set()
    diag_desc = set()
    cols = set()

    def solve(row=0):
        # Base case, udalo nam sie wypelnic wszystkie wiersze
        # czyli wykorzystalismy kazdego z 8 hetmanow.
        if row == 8:
            return 1

        total = 0

        for c in range(8):
            # Skip szachowanego juz pola.
            if row + c in diag_asc or row - c in diag_desc or c in cols:
                continue

            diag_asc.add(row + c)
            diag_desc.add(row - c)
            cols.add(c)

            total += solve(row + 1)

            # Back track
            diag_asc.remove(row + c)
            diag_desc.remove(row - c)
            cols.remove(c)

        return total

    return solve()


print(queens())
