from math import inf


def solve(T1, T2):
    nt1 = len(T1)
    indexes = [0 for _ in range(nt1)]
    idx = 0

    # Dopoki nie skonczymy przegladac kazdego wiersza
    # (=> indeks dla jakiegos wiersza jest < nt1)
    while min(indexes) < nt1:
        smallest = inf

        # Szukamy najmniejszego elementu
        for i in range(nt1):
            if indexes[i] not in range(nt1):
                continue

            current = T1[i][indexes[i]]

            if current < smallest:
                smallest = current

        # Zwiększamy indeks o 1 dla kazdego wiersza, ktory
        # ma ten element (nie chcemy go wpisac 2 razy to T2)
        for i in range(nt1):
            if indexes[i] not in range(nt1):
                continue

            if T1[i][indexes[i]] == smallest:
                indexes[i] += 1

        # Wpisujemy element do T2
        T2[idx] = smallest
        idx += 1

    print(T2)


T1 = [[1, 2, 3], [3, 4, 5], [3, 4, 7]]
solve(T1, [0 for _ in range(len(T1) ** 2)])
