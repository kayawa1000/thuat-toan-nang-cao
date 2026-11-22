import bisect
def lDS2(arr):

    tails = []
    neg_tails = []

    for x in arr:
        neg_x = -x
        pos = bisect.bisect_left(neg_tails, neg_x)
        if pos == len(tails):
            tails.append(x)
            neg_tails.append(neg_x)
        else:
            tails[pos] = x
            neg_tails[pos] = neg_x

    return len(tails)