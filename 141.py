def weights(T, mass, s=0):
    if mass == 0:
        return True

    if s >= len(T) or mass < 0:
        return False

    return (
        # nie bierzemy odwaznika
        weights(T, mass, s + 1)
        # bierzemy odwaznik
        or weights(T, mass - T[s], s + 1)
        # odkladamy na 2 szalke
        or weights(T, mass + T[s], s + 1)
    )


print(weights([1, 3, 9, 27], 23))
