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
    
    with open('Токарев Александр Александрович_У-224_vvod_1.txt', 'r') as f:
        matrix = [[float(num) for num in line.split(' ')] for line in f]
    print(matrix)

    printMatrix(matrix)
    answer = str(sumLineWithMinValue(matrix))
    print(f'Summary of line with min value = {sumLineWithMinValue(matrix)}')
    with open('Токарев Александр Александрович_У-224_vivod_1.txt', 'w') as f:
        f.write(f'Сумма строки с минимальным значением = {answer}')


if(__name__ == '__main__'):
    main()