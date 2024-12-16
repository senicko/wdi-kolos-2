def in_bounds(r, c, n):
    return 0 <= r < n and 0 <= c < n


def flip(mirror):
    return "/" if mirror == "\\" else "\\"


def bounce(move, mirror):
    return (move[1], move[0]) if mirror == "\\" else (-1 * move[1], -1 * move[0])


def napraw(ogrod, at=(0, 0), move=(1, 0), flips=0):
    n = len(ogrod)
    r, c = at

    while in_bounds(r, c, n):
        mirror = ogrod[r][c]

        if mirror != " ":
            move = bounce(move, mirror)
            fixed = napraw(ogrod, (r + move[0], c + move[1]), move, flips)

            if not fixed and flips < 2:
                mirror = flip(mirror)
                move = bounce(move, mirror)

                ogrod[r][c] = mirror
                napraw(ogrod, (r + move[0], c + move[1]), move, flips + 1)
                ogrod[r][c] = flip(mirror)

            break

        r += move[0]
        c += move[1]

    # We can see the guy on the other side
    if (r, c) == (n, n - 1):
        print(*ogrod, sep="\n")
        return True


ogrod = [
    [" ", " ", " ", " ", " "],
    [" ", "/", " ", "\\", " "],
    [" ", " ", " ", " ", " "],
    ["\\", " ", " ", "/", " "],
    [" ", "/", " ", " ", "/"],
]

napraw(ogrod)
