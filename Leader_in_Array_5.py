def find_leaders(arr):
    n = len(arr)
    if n == 0:
        return []

    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1]

arr = list(map(int, input().split()))
leaders = find_leaders(arr)
print("Leaders:", leaders)
