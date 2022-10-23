def f():
    N = int(input("Enter integer number: "))
    if (N >= 1):

        count = 0
        two_in_sqrt = 1

        while (two_in_sqrt < N):
            two_in_sqrt *= 2
            count += 1

            if (two_in_sqrt > N):
                count -= 1
                two_in_sqrt = 1

                for _ in range(1, count+1):
                    two_in_sqrt *= 2

        print(f'The largest integer power of two is: {two_in_sqrt}')
        print(f'The maximum degree number is: {count}')

    else:
        print("You enter small number")
f()