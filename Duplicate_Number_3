def findDuplicate(arr):
    low = 1
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        count = sum(x <= mid for x in arr)
        if count > mid:
            high = mid
        else:
            low = mid + 1
    return low

arr = list(map(int, input().split()))
print(findDuplicate(arr))
