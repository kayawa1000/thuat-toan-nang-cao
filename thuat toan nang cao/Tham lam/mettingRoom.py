def mettingRoom(s, f):
    meetings = sorted(zip(f, s))
    count = 0
    last_end = -1

    for end, start in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    return count