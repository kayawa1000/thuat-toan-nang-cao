def sumOfOnes(n, l, r):
    len_cache = {0: 1, 1: 1}

    def get_len(x):
        if x in len_cache:
            return len_cache[x]
        res = 2 * get_len(x // 2) + 1
        len_cache[x] = res
        return res

    def count_ones(x, a, b):
        if a > b or x == 0:
            return 0
        if x == 1:
            return b - a + 1

        half_len = get_len(x // 2)
        mid_pos = half_len + 1
        total = 0

        if a <= half_len:
            total += count_ones(x // 2, a, min(b, half_len))

        if a <= mid_pos <= b and (x % 2 == 1):
            total += 1

        if b > mid_pos:
            right_a = max(a, mid_pos + 1) - mid_pos
            right_b = b - mid_pos
            total += count_ones(x // 2, right_a, right_b)

        return total

    return count_ones(n, l, r)

