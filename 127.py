from math import inf


def multi(T):
    maximum = -inf

    for w in T:
        for i in range(1, len(w) // 2):
            if len(w) % i == 0 and w[:i] * (len(w) // i) == w:
                maximum = max(maximum, len(w))

    return maximum if maximum != -inf else 0


print(multi(["ABCABCABC", "AAAA", "ABAABA"]))
