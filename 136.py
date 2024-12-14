def knight_problem(n, r, c):
    # Tworzymy tablice 2d w ktorej trzymamy ktore pola zostaly
    # juz odwiedzone.
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Od razu odwiedzamy wierzcholek startowy.
    visited[r][c] = True

    # Funkcja do dostawania ruchow.
    def get_move(r, c, i):
        moves_r = [1, 1, -1, -1, 2, 2, -2, -2]
        moves_c = [-2, 2, 2, -2, -1, 1, 1, -1]

        mr = moves_r[i]
        mc = moves_c[i]

        if r + mr in range(n) and c + mc in range(n) and not visited[r + mr][c + mc]:
            return (mr, mc)

        return None

    def rec(r, c, moves=1):
        # Jezeli wykonalismy n*n ruchow to odwiedzilismy kazde
        # pole na tablicy.
        if moves == n * n:
            return 1

        count = 0

        for i in range(8):
            if move := get_move(r, c, i):
                mr, mc = move

                # Backtracking
                visited[r + mr][c + mc] = True
                count += rec(r + mr, c + mc, moves + 1)
                visited[r + mr][c + mc] = False

        return count

    return rec(r, c)


print(knight_problem(5, 0, 0))
