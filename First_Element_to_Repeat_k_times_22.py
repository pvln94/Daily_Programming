def first_element_to_repeat_k_times(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == k:
            return num
    return -1

arr = list(map(int, input().split()))
k = int(input())
print(first_element_to_repeat_k_times(arr, k))
