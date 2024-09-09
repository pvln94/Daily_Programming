def S(x):
    if x:
        l = 0
        m = 0
        h = len(x) - 1
        
        while m <= h:
            if x[m] == 0:
                x[l], x[m] = x[m], x[l]
                l += 1
                m += 1
            elif x[m] == 1:
                m += 1
            else: 
                x[h], x[m] = x[m], x[h]
                h -= 1
        print(x)
    else:
        print([])  

if __name__ == "__main__":
    n = input()
    a = list(map(int, n.split())) if n else []
    S(a)
