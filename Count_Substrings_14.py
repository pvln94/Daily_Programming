def count_substrings_with_k_distinct_hashmap(s, k):
    n = len(s)
    count = 0
    for i in range(n):
        char_count = {}
        distinct_count = 0
        for j in range(i, n):
            if char_count.get(s[j], 0) == 0:
                distinct_count += 1
            char_count[s[j]] = char_count.get(s[j], 0) + 1

            if distinct_count > k:
                break
            if distinct_count == k:
                count += 1
    return count

s = input()
k = int(input())
print(count_substrings_with_k_distinct_hashmap(s, k))
