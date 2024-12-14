def sum_of_terms(n, ans="", prev=1):
    # Jak nasza liczba jest rowna 0 to wypisujemy wynik
    if n == 0:
        ans = ans[1:]
        # omijamy sama liczbe wejsciowa (np podzial 20 na 20)
        if "+" in ans:
            print(ans)
        return

    for term in range(prev, n + 1):
        if n - term >= 0:
            sum_of_terms(n - term, f"{ans}+{term}", term)


sum_of_terms(10)
