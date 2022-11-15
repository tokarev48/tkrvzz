from random import randint

N = int(input('Enter the size of matrixes: '))
def findMax(matrix):
    max = 0
    for i in range(N):
        for j in range(N):
            if(matrix[i][j] > max):
                max = matrix[i][j]
    return max


def replaceMaxValues(matrixA, matrixB):
    max_A = findMax(matrixA)
    max_B = findMax(matrixB)
    for i in range(N):
        for j in range(N):
            if(matrixA[i][j] == max_A):
                matrixA[i][j] = max_B
            if(matrixB[i][j] == max_B):
                matrixB[i][j] = max_A


def printMatrix(matrix):
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()
    print()


def main():
    matrix_A = [[randint(1,100) for i in range(N)] for j in range(N)]
    matrix_B = [[randint(1,100) for i in range(N)] for j in range(N)]
    print(f'Max value in matrix A: {findMax(matrix_A)}')
    print(f'Max value in matrix B: {findMax(matrix_B)}')
    print('Before replacement\nMatrix A:')
    printMatrix(matrix_A)
    print('Matrix B:')
    printMatrix(matrix_B)
    replaceMaxValues(matrix_A, matrix_B)
    print('After replacement\nMatrix A:')
    printMatrix(matrix_A)
    print('Matrix B:')
    printMatrix(matrix_B)




if(__name__ == '__main__'):
    main()

