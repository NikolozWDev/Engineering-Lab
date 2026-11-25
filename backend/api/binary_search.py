def bsearch(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        lo, hi = (mid + 1, hi) if arr[mid] < target else (lo, mid - 1)
    return -1

print(bsearch([1, 3, 5, 7, 9, 11], 7))  # 4
