def longest_palindrome_substring(s):
    n = len(s)
    max_len = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            is_palindrome = True
            left = i
            right = j
            while left < right:
                if s[left] != s[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1

            if is_palindrome and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1

    result = ""
    for k in range(start, start + max_len):
        result += s[k]

    return result

input_str = input()
print(longest_palindrome_substring(input_str))
