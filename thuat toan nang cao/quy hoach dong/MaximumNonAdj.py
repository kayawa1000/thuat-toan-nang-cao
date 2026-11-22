def maximumNonAdj(arr):
    prev2 = 0
    prev1 = 0

    for x in arr:
        cur = prev1
        if prev2 + x > cur:
            cur = prev2 + x
        if cur < 0:
            cur = 0
        prev2, prev1 = prev1, cur

    return prev1