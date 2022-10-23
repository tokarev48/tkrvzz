def f():
    n = int(input())
    fac = 1
    sum = 0
    for i in range(1, n + 1):
        fac = fac * i
        sum = sum + fac
    print(sum)
f()