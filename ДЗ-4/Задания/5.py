def f ():
    sum = 0
    n = int(input())
    for i in range(1, n + 1):
        sum = sum + (i ** 3)
    print(sum)
f()