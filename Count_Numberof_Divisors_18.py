import math

def count_divisors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i == N // i:
                count += 1
            else:
                count += 2
    return count

N = int(input())
print(count_divisors(N))
