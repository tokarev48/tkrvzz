primeNums = []

def isPrime(num):
    if (num == 1):
        return True
    for i in range(2, num):
        if (num%i == 0):
            return False
    return True


def createListOfPrimes(n):
    for i in range(n, 2*n):
        if(isPrime(i)):
            primeNums.append(i)

    
def outputPrimeTwins(certainList):
    for i in range(len(certainList)-1):
        if((certainList[i+1] - certainList[i]) == 2):
            print(f'\nPair: {certainList[i]} {certainList[i+1]}')


def main():
    n = 0
    while(n < 3): n = int(input('Enter n value: '))
    createListOfPrimes(n)
    outputPrimeTwins(primeNums)


if(__name__ == '__main__'):
    main()