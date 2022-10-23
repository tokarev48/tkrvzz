def f():
    numbers=[]
    i = 1

    while True:
        try:
            num = None
            num = int(input(f"Enter the {i} number: "))
            i += 1

            if (num == 0):
                break

            numbers.append(num)

        except ValueError:
            print("You enter a wrong data")

    max = 0
    ex_max = 0
    ex_num = None

    for num in numbers:
        if (ex_num == num):
            max += 1
        else:
            if (ex_max < max):
                ex_max = max
            max = 0
        ex_num = num

    print(f"The maximum sequence of equal numbers is: {ex_max}")
f()