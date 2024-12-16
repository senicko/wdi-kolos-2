from math import isqrt


def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def A(n):
    t = 1
    d = 2

    while d * d < n:
        if n % d == 0:
            t += d + n // d
        d += 1

    if d * d == n:
        t += d

    return t


def B(n):
    a = 1
    b = 1

    while a < n:
        a, b = b, a + b

    return a


def C(n):
    revers = 0
    n_copy = n

    while n_copy > 0:
        revers = revers * 10 + n_copy % 10
        n_copy //= 10

    return n + revers


def cycle(x, n):
    def rec(current, steps=0):
        if 1 <= steps <= n and current == x:
            return steps

        if steps == n:
            return 0

        a = rec(A(current), steps + 1)
        if a != 0:
            return a

        b = rec(B(current), steps + 1)
        if b != 0:
            return b

        c = rec(C(current), steps + 1)
        if c != 0:
            return c

        return 0

    return rec(x)


print(cycle(29, 6))
print(B(29))
