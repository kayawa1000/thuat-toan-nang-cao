def numberOfSubArray(arr):
    n = len(arr)
    if n == 0:
        return 0

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    candidate_sums = set()
    for i in range(n):
        for j in range(i, n):
            candidate_sums.add(prefix[j + 1] - prefix[i])

    ans = 0
    for target in candidate_sums:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i):
                if prefix[i] - prefix[j] == target:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        if dp[n] > ans:
            ans = dp[n]

    return ans