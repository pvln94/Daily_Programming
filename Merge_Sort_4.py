def merge_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            
            k = 1
            while k < n and arr2[k] < first:
                arr2[k - 1] = arr2[k]
                k += 1
            arr2[k - 1] = first

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merge_sorted_arrays(arr1, arr2)

print(arr1)
print(arr2)
