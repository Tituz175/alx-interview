#!/usr/bin/python3
"""
sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def rotate_2d_matrix(matrix):
    """
    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    # reversing the matrix
    for _ in range(3):
        for i in range(len(matrix)):
            matrix[i].reverse()

        # make transpose of the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):

                # swapping mat[i][j] and mat[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
