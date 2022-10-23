def f():
    a = int(input("enter a number 1: "))
    b = int(input("enter a number 2: "))
    if b > a:    
        for i in range(a, b+1):
            print(i)
    else:
       for i in range (b, a+1):
            print(i)
f()