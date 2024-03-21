#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    i = 0
    for fir in matrix:
        j = 0
        new_matrix[i] = matrix[i].copy()
        for sec in fir:
            sec = int(sec)
            new_matrix[i][j] = sec ** 2
            j = j + 1
        i = i + 1
    return new_matrix


if __name__ == '__main__':
    square_matrix_simple(matrix=[])
