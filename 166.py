def solve(shards_a, shards_b):
    def permutations(t, i=0):
        if i == len(t):
            return ["".join(t)]

        result = []

        for j in range(i, len(t)):
            t[i], t[j] = t[j], t[i]
            result += permutations(t, i + 1)
            t[i], t[j] = t[j], t[i]

        return result

    permutations_a = permutations(shards_a)
    permutations_b = permutations(shards_b)

    for a in permutations_a:
        if a in permutations_b:
            return True

    return False


print(solve(["ab", "cde", "cfed", "fab"], ["abc", "abc", "def", "fed"]))
