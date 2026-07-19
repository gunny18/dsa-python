"""
- Given a nxn matrix, rotate it 90deg clockwise

Approach 1:
    - This approach involves 2 operations on the matrix
        - Transpose
        - Reverse each row
    - Transpose
        - The logic is optimised, but at the end of the day TC is O(n^2)
    - Reverse each row
        - Here again TC is O(n^2)
    TC -> O(2n^2) ~~ O(n^2)
    SC -> O(1)

What can be improved ?
    - Check transpose logic, to see if it can be made simpler!

Brute Force Approach:
    - This is where we crete an empty answer matrix
    - We then map input matrix indexes to output rotated matrix and just insert elements.
    - Key here is to find the index relations (Easy, do it on pen and paper)
    - TC -> O(n^2)
    - SC -> O(n^2)
        - SC is what we have optimised for in above approach 1
"""


def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        swaps = n - i - 1
        if swaps != 0:
            for j in range(n - 1, -1, -1):
                if swaps != 0:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    swaps -= 1
                else:
                    break


def reverse_matrix_rows(matrix):
    n = len(matrix)
    for i in range(n):
        start, end = 0, n - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1


def rotate_matrix_by_90_deg(matrix):
    transpose_matrix(matrix)
    reverse_matrix_rows(matrix)
    return matrix


print(rotate_matrix_by_90_deg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate_matrix_by_90_deg([[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]))
