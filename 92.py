def spiral(T):
    n = len(T)

    start = 0
    end = n - 1
    num = 1

    # Zmniejszamy rozmiar "wewnetrznego kwadratu"
    while start <= end:
        # Wypełniamy gorny brzeg aktualnego kwadratu
        for i in range(start, end + 1):
            T[start][i] = num
            num += 1

        # prawy brzeg aktualnego kwadratu
        for i in range(start + 1, end + 1):
            T[i][end] = num
            num += 1

        # dolny brzeg aktualnego kwadratu
        for i in range(end - 1, start - 1, -1):
            T[end][i] = num
            num += 1

        # lewy brzeg aktualnego kwadratu
        for i in range(end - 1, start, -1):
            T[i][start] = num
            num += 1

        start += 1
        end -= 1

    print(*T, sep="\n")


spiral([[0 for _ in range(4)] for _ in range(4)])
