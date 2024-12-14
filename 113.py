def subtract(a, b):
    n = len(a)
    borrow = 0

    for i in range(n - 1, -1, -1):
        diff = a[i] - b[i] - borrow
        if diff < 0:
            diff += 2
            borrow = 1
        else:
            borrow = 0

        a[i] = diff

    return a


def gt(a, b):
    n = len(a)

    for i in range(n):
        if a[i] == b[i]:
            continue

        return a[i] > b[i]

    return False


def distance(T):
    n = len(T)

    max = None
    start = None
    end = None

    for i in range(n):
        for j in range(i + 1, n):
            a = T[i]
            b = T[j]

            if gt(b, a):
                a, b = b, a

            difference = subtract(a, b)

            if max is None:
                max = difference
                start = i
                end = j

            elif gt(difference, max):
                max = difference
                start = i
                end = j

    return end - start


print(
    distance(
        [
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 0, 0, 0],
        ]
    )
)
