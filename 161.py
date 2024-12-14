def count_ones(n):
    count = 0
    while n > 1:
        count += n % 2
        n //= 2
    return count


def solve(T, a=0, b=0, c=0, s=0):
    # Zamieniamy liczby na ilosc 1 uzytych do ich zapisu
    # zeby zbierac sobie tylko sumy ilosci jedynek
    T = [count_ones(x) for x in T]

    if s == len(T):
        if a == b == c:
            return True
        return False

    # Dla kazdego elementu podejmujemy 3 decyzje
    return (
        solve(T, a + T[s], b, c, s + 1)
        or solve(T, a, b + T[s], c, s + 1)
        or solve(T, a, b, c + T[s], s + 1)
    )


print(solve([2, 3, 5, 7, 15]))
