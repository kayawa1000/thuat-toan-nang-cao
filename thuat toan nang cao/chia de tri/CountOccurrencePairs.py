def countOccurrencePairs(arr):
    n = len(arr)
    if n < 2:
        return 0

    left_cnt = [0] * n
    freq_l = {}
    for i in range(n):
        v = arr[i]
        c = freq_l.get(v, 0) + 1
        freq_l[v] = c
        left_cnt[i] = c

    right_cnt = [0] * n
    freq_r = {}
    for j in range(n - 1, -1, -1):
        v = arr[j]
        c = freq_r.get(v, 0) + 1
        freq_r[v] = c
        right_cnt[j] = c

    temp = [0] * n

    def merge_count(l, r):
        if l >= r:
            return 0
        mid = (l + r) // 2
        inv = merge_count(l, mid) + merge_count(mid + 1, r)

        p = l
        for q in range(mid + 1, r + 1):
            target = right_cnt[q]
            while p <= mid and left_cnt[p] <= target:
                p += 1
            inv += mid - p + 1

        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if left_cnt[i] <= right_cnt[j]:
                temp[k] = left_cnt[i]
                i += 1
            else:
                temp[k] = right_cnt[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = left_cnt[i]
            i += 1
            k += 1
        while j <= r:
            temp[k] = right_cnt[j]
            j += 1
            k += 1

        left_cnt[l : r + 1] = temp[l : r + 1]
        return inv

    return merge_count(0, n - 1)
    