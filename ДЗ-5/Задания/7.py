def f():
    numbers = []
    i = 1

    while True:
        num = None

        try:
            num = int(input(f"Enter the {i} number: "))

            i += 1
            if (num != 0):
                numbers.append(num)
            else:
                break

        except ValueError:
            print("You enter a wrong data")


    ex_num = numbers[0]
    k = 0
    for num in numbers:
        if (ex_num < num):
            k += 1

    print(f"The number of elements bigest than the previous one is: {k}")
f()