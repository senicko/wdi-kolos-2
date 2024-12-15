def solve(shards_a, shards_b):
    len_a = len(shards_a)
    len_b = len(shards_b)

    used_a = [0 for _ in range(len(shards_a))]
    used_b = [0 for _ in range(len(shards_b))]

    def rec(word_a="", word_b=""):
        if min(used_a) == 1 and min(used_b) == 1:
            return word_a == word_b

        possible = False

        for i in range(len_a):
            if used_a[i] == 0:
                used_a[i] = 1
                possible = possible or rec(word_a + shards_a[i], word_b)
                used_a[i] = 0

        for i in range(len_b):
            if used_b[i] == 0:
                used_b[i] = 1
                possible = possible or rec(word_a, word_b + shards_b[i])
                used_b[i] = 0

        return possible

    return rec()


print(solve(["ab", "cde", "cfed", "fab"], ["abc", "abc", "def", "fed"]))
