from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        anagram_map[sorted_str].append(s)
    return list(anagram_map.values())

input_str = input()
strs = [s.strip() for s in input_str.split(',')]
print(group_anagrams(strs))
