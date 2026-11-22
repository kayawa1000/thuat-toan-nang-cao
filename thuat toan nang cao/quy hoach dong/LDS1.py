def lDS1(arr):
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n
    best = 1

    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
        if dp[i] > best:
            best = dp[i]

    return best