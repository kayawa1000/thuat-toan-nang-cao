def numberOfDistinctString(s, c):
    n = len(s)
    distinct = set()

    def backtrack(idx, cur):
        if idx == n:
            distinct.add("".join(cur))
            return

 
        cur.append(c)
        cur.append(s[idx])
        backtrack(idx + 1, cur)
        cur.pop()
        cur.pop()


        cur.append(s[idx])
        backtrack(idx + 1, cur)
        cur.pop()


    def bt_positions(idx, cur):
        if idx == n:

            distinct.add("".join(cur))
            distinct.add("".join(cur) + c)
            return

        cur.append(c)
        cur.append(s[idx])
        bt_positions(idx + 1, cur)
        cur.pop()
        cur.pop()

        cur.append(s[idx])
        bt_positions(idx + 1, cur)
        cur.pop()

    bt_positions(0, [])
    return len(distinct)