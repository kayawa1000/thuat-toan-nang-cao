def combinationSum(arr,k):
    a = sorted(arr)
    n = len(a)
    count = [0]

    def backtrack(idx, cur_sum):
        if cur_sum == k:
            count[0] += 1

        for i in range(idx, n):
            if i > idx and a[i] == a[i - 1]:
                continue
            backtrack(i + 1, cur_sum + a[i])

    backtrack(0, 0)
    return count[0]