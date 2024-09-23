def Longest_Substring(S):
    start, max_length = 0, 0
    char_index_map = {}
    
    for end, char in enumerate(S):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


A = input()
print(Longest_Substring(A))

