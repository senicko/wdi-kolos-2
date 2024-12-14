def weight(T, mass, s=0, choices=[]):
    if mass == 0:
        print(choices)
        return True

    if s >= len(T) or mass < 0:
        return False

    return weight(T, mass, s + 1, choices[:]) or weight(
        T, mass - T[s], s + 1, choices + [T[s]]
    )


print(weight([1, 3, 9, 2, 7], 5))
