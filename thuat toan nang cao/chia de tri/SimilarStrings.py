from collections import Counter


def similarStrings(a, b):
    if len(a) != len(b):
        return False

    memo = {}

    def check(i, j, length):
        key = (i, j, length)
        if key in memo:
            return memo[key]

        sub_a = a[i : i + length]
        sub_b = b[j : j + length]

        if sub_a == sub_b:
            memo[key] = True
            return True

        if length % 2 == 1:
            memo[key] = False
            return False

        if Counter(sub_a) != Counter(sub_b):
            memo[key] = False
            return False

        half = length // 2
        res = (check(i, j, half) and check(i + half, j + half, half)) or (
            check(i, j + half, half) and check(i + half, j, half)
        )
        memo[key] = res
        return res

    return check(0, 0, len(a))

