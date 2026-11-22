def nthPermutation(n, k):
    used = [False] * (n + 1)
    path = []
    res = []
    count = [0]

    def backtrack():
        if res:
            return
        if len(path) == n:
            count[0] += 1
            if count[0] == k:
                res.extend(path)
            return

        for x in range(1, n + 1):
            if not used[x]:
                used[x] = True
                path.append(x)
                backtrack()
                path.pop()
                used[x] = False
                if res:
                    return

    backtrack()
    return res