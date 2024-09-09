def S(x):
    if x:
        x.sort()
        print(x)
    else:
        print(x)  

if __name__ == "__main__":
    n = input()
    a = list(map(int, n.split())) if n else []
    S(a)
