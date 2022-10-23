def f():
    x = int(input("Enter amount of kilometers in first day: "))
    y = int(input("Enter amount of kilometers: "))

    i = 1

    while x < y:
        x *= 1.1
        i += 1

    print(i)
f()