def easyLeo(n,m):
    MOD = 10**9 + 7
    ways = [0] * (m + 1)
    ways[0] = 1

    for j in range(1, m + 1):
        s = ways[j - 1]
        if j >= 2:
            s += ways[j - 2]
        if j >= 3:
            s += ways[j - 3]
        if j >= 4:
            s += ways[j - 4]
        ways[j] = s % MOD

    return pow(ways[m], n, MOD)