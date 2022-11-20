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
    if(minColumn + 1 == len(matrix)):
        print(f'Column = {minColumn + 1} will be switched with column {minColumn}')
    else:
        print(f'Column = {minColumn + 1} will be switched with column {minColumn + 2}')
    for i in range(len(matrix)):
        if(minColumn + 1 == len(matrix)):
            temp = matrix[i][minColumn]
            matrix[i][minColumn] = matrix[i][minColumn-1] 
            matrix[i][minColumn-1] = temp
        else:
            temp = matrix[i][minColumn]
            matrix[i][minColumn] = matrix[i][minColumn+1] 
            matrix[i][minColumn+1] = temp


def main():
    with open('Токарев Александр Александрович_У-224_vvod_2.txt', 'r') as f:
        matrix = [[int(num) for num in line.split(' ')] for line in f]
    print('Before switch:')
    printMatrix(matrix)
    switchColumns(matrix)
    print('After switch:')
    printMatrix(matrix)

    with open('Токарев Александр Александрович_У-224_vivod_2.txt', 'w') as f:
        f.write('Преобразовання матрица:\n')
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                f.write(str(matrix[i][j]))
                f.write(' ')
            f.write('\n')


if(__name__ == '__main__'):
    main()