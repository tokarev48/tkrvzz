def f():
    N = int(input("Enter integer number: "))

    if (N >= 2):
        for i in range(2, N+1):
            if (N % i == 0):
                print(f"The smallest natural divisor is: {i}")
                break
f()