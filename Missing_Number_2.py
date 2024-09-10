def find_missing_number(arr):
    n = len(arr) + 1
    if n == 2:
        return 1 if arr[0] == 2 else 2
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    missing_number = total_sum - array_sum
    return missing_number

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print("Missing Number:", find_missing_number(arr))
