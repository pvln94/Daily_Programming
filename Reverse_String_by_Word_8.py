s = input()
n = len(s)
result = []
word = []
i = 0

while i < n:
    while i < n and s[i] == ' ':
        i += 1
    if i >= n:
        break
    word_start = i
    while i < n and s[i] != ' ':
        i += 1
    word = []
    for j in range(word_start, i):
        word.append(s[j])
    result.insert(0, ''.join(word))

if not result:  
    print('')
else:
    output = []
    for i in range(len(result)):
        if i > 0:
            output.append(' ')
        output.extend(result[i])
    print(''.join(output))
