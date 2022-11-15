from random import uniform


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end='  ')
        print()


def sumLineWithMinValue(matrix):
    min = matrix[0][0]
    line = 0
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] < min):
                line = i
                min = matrix[i][j]
    for i in range(len(matrix)):
        sum += matrix[line][i]
    return sum


def main():
    
    n = int(input('Enter the size of matrix: '))
    matrix = [[round(uniform(1,101), 2) for i in range(n)] for j in range(n)]
    printMatrix(matrix)
    print(f'Summary of line with min value = {sumLineWithMinValue(matrix)}')


if(__name__ == '__main__'):
    main()