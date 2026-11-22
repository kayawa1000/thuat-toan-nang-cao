def maximizeSum(arr):
    n = len(arr)
    if n <= 1:
        return 0

    arr_sorted = sorted(arr)
    k = n // 2

    max_part = sum(arr_sorted[n - k :])
    min_part = sum(arr_sorted[:k])

    return 2 * (max_part - min_part)