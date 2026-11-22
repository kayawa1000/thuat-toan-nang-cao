def fibLikeSq(n):
    MOD = 10**9 + 7
    if n == 1 or n == 2:
        return 1 % MOD
    if n == 3:
        return 2 % MOD

    a, b, c = 1, 1, 2  # f(1), f(2), f(3)
    for _ in range(4, n + 1):
        nxt = (c * b + a) % MOD
        a, b, c = b, c, nxt

    return c