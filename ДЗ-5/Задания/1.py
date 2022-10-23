def f():
    try:

        N = abs(int(input("Enter integer number: ")))

        for _ in range(1, N+1):
            print(_**2)

    except ValueError:
        print("You etner a wrong number")
f()
