def f():
    numbers = []

    i = 1
    while True:
        num = None

        try:
            num = int(input(f"Enter the {i} non-negative number: "))

            if (num >= 0):
                i += 1
                if (num != 0):
                    numbers.append(num)
                else:
                    break
            else:
                print("You enter a wrong number")
        except ValueError:
            print("You enter a wrong data")

    print(f"You have {len(numbers)} numbers in sequence")
f()
