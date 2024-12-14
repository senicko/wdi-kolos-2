def sum_of_terms(n, previous_term=1, ans=""):
    # Base case
    if n == 0:
        ans = ans[1:]
        # Nie chcemy wypisac rozkladu liczby na sama siebie
        if "+" in ans:
            print(ans)
        return

    # Jezeli dalej mamy cos do odejmowania
    for term in range(previous_term, n + 1):
        sum_of_terms(n - term, term, f"{ans}+{term}")


sum_of_terms(4)
