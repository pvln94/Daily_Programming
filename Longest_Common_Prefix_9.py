def longest_common_prefix(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]

strs = input().split()

result = longest_common_prefix(strs)
print(result)
