def weight(T, mass, s=0, choices=[]):
    # Base case'y
    if mass == 0:
        print(choices)
        return True

    if mass < 0:
        return False

    for i in range(s, len(T)):
        # Dla kazdego odwaznika podejmujemy decyzje
        return weight(T, mass, i + 1, choices[:]) or weight(
            T, mass - T[i], i + 1, choices + [T[i]]
        )


print(weight([1, 3, 9, 2, 7], 5))
