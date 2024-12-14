def nki(T, product, nka, start=0, ans=""):
    n = len(T)

    # Base case
    if nka == 1:
        for i in range(start, n):
            if T[i] == product:
                # Zliczamy "liscie" w drzewie
                # wywolan rekurencyjnych, ktore
                # koncza poprawna sciezke.
                print(ans, T[i])
                return 1

        return 0

    total = 0

    # Szukamy liczb ktore moga wchodzic w sklad n-ek
    # i dzielimy problem na mniejszy.
    for i in range(start, n):
        if product % T[i] == 0:
            total += nki(T, product // T[i], nka - 1, i, f"{ans} {T[i]}")

    return total


print("liczba n-ek:", nki([2, 2, 2, 2, 2, 5, 5, 5, 5], 10, 2))
