def hanoi(discs, a="A", b="B", c="C"):
    # Base case. Jest jeden sposob na przeniesienie
    # jednego dysku miedzy kijkami.
    if discs == 1:
        return 1

    # Przenosimy n-1 dyskow z kijka A na C przy pomocy B
    total = hanoi(discs - 1, a, c, b)

    # Przenosimy najwiekszy dysk z A na B
    total += 1

    # Przenosimy n-1 dyskow z C na B przy pomocy A
    total += hanoi(discs - 1, c, b, a)

    return total


print(hanoi(3))
