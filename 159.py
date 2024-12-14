from math import isqrt


# is prime
def is_prime(n):
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, isqrt(n) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def solve(A, B, current=0, ans=""):
    # Chcemy miec 1 z przodu
    if current == 0:
        return solve(A - 1, B, 1, "1")

    # Base case
    if A == 0 and B == 0:
        if not is_prime(current) and current != 1:
            print(ans)
            return 1
        return 0

    # Wywolanie rekurencyjne
    count = 0
    if A > 0:
        count += solve(A - 1, B, current * 2 + 1, ans + "1")
    if B > 0:
        count += solve(A, B - 1, current * 2, ans + "0")

    return count


print(solve(2, 3))
