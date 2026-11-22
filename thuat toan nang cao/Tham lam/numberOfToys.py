def numberOfToys(arr, k):
    arr.sort()
    count = 0

    for price in arr:
        if k >= price:
            k -= price
            count += 1
        else:
            break

    return count