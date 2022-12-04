def reversedNumber(number):
    if(number > 0):
        print(number%10, end='')
        reversedNumber(number//10)
    else:
        return 0


def main():
    reversedNumber(736251)


if(__name__ == '__main__'):
    main()