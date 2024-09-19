def heaps_algorithm(n, array, results):
    if n == 1:
        results.add(''.join(array))
    else:
        for i in range(n):
            heaps_algorithm(n - 1, array, results)
            if n % 2 == 0:
                array[i], array[n - 1] = array[n - 1], array[i]
            else:
                array[0], array[n - 1] = array[n - 1], array[0]

string = input()
permutations = set()
heaps_algorithm(len(string), list(string), permutations)

sorted_permutations = sorted(permutations)
print(sorted_permutations)
