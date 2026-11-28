def countInversions(arr):
    def merge_sort(nums):
        n = len(nums)
        if n <= 1:
            return nums, 0

        mid = n // 2
        left, inv_left = merge_sort(nums[:mid])
        right, inv_right = merge_sort(nums[mid:])

        merged = []
        inv = inv_left + inv_right
        i = j = 0
        len_l = len(left)
        len_r = len(right)

        while i < len_l and j < len_r:
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len_l - i
                j += 1

        if i < len_l:
            merged.extend(left[i:])
        if j < len_r:
            merged.extend(right[j:])

        return merged, inv

    _, total_inv = merge_sort(arr)
    return total_inv


