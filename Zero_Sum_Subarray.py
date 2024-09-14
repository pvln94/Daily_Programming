def find_subarrays_with_zero_sum(arr):
    cumulative_sum_map = {}
    cumulative_sum = 0
    result = []

    for i in range(len(arr)):
        cumulative_sum += arr[i]
        if cumulative_sum == 0:
            result.append((0, i))
        if cumulative_sum in cumulative_sum_map:
            start_indices = cumulative_sum_map[cumulative_sum]
            for start_index in start_indices:
                result.append((start_index + 1, i))
        if cumulative_sum in cumulative_sum_map:
            cumulative_sum_map[cumulative_sum].append(i)
        else:
            cumulative_sum_map[cumulative_sum] = [i]

    return result

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
print(find_subarrays_with_zero_sum(arr))
