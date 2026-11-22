def maximalMultiple(arr):
    n = len(arr)
    best = None

    def backtrack(idx, sum1, cnt1, sum2, cnt2):
        nonlocal best
        if idx == n:
            if cnt1 > 0 and cnt2 > 0:
                prod = sum1 * sum2
                if best is None or prod > best:
                    best = prod
            return

        backtrack(idx + 1, sum1 + arr[idx], cnt1 + 1, sum2, cnt2)

        backtrack(idx + 1, sum1, cnt1, sum2 + arr[idx], cnt2 + 1)

    backtrack(0, 0, 0, 0, 0)
    return best