def D(n):


    n = int(input())
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(3, n + 1):
            D(i) = (n - 1) * (D(i - 1) + D(i - 2))
        return D(n)
    print(D(n) % 1000000007)
