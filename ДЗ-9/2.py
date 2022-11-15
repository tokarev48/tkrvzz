from random import randint


def minMult(matrix):
    column = 0
    mult = 1
    min = 10000000
    for i in range(len(matrix)):
        mult = 1
        for j in range(len(matrix)):        
            mult *= matrix[j][i]
        if (mult < min):
            min = mult
            column = i
    return column


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()


def switchColumns(matrix):
    minColumn = minMult(matrix)
    print(f'Column = {minColumn + 1} will be switched with column {minColumn + 2}')
    for i in range(len(matrix)):
        if(minColumn+1 == len(matrix)):
            temp = matrix[i][minColumn]
            matrix[i][minColumn] = matrix[i][minColumn-1] 
            matrix[i][minColumn-1] = temp
        else:
            temp = matrix[i][minColumn]
            matrix[i][minColumn] = matrix[i][minColumn+1] 
            matrix[i][minColumn+1] = temp


def main():
    n = int(input('Enter size of matrix: '))
    matrix = [[randint(1, 10) for i in range(n)] for j in range(n)]
    print('Before switch:')
    printMatrix(matrix)
    switchColumns(matrix)
    print('After switch:')
    printMatrix(matrix)


if(__name__ == '__main__'):
    main()