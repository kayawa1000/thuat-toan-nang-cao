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
        count = 0
        i = 0
        while i < n:
            found_end = -1
            for j in range(i, n):
                if prefix[j + 1] - prefix[i] == target:
                    found_end = j
                    break
            if found_end != -1:
                count += 1
                i = found_end + 1
            else:
                i += 1
        if count > ans:
            ans = count

    return ans