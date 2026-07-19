"""
- Given n, return matrix containing first n rows of pascal triangle

Approach 1:
    - Say I use nCr
    - For each row
        - Use nCr to find each column
    TC -> n*n*n --> O(n^3)

Approach 2:
    - Using the previous logic of just computing extra multipliers and computing the row
    - TC -> O(n^2)
"""


def get_pascal_row(r):
    row = [1]
    prev = 1
    for i in range(1, r):
        prev = prev * (r - i)
        prev = prev // i
        row.append(prev)
    return row


def pascal_triangle_app1(n):
    pascal_matrix = []
    for i in range(1, n + 1):
        row = get_pascal_row(i)
        pascal_matrix.append(row)
    return pascal_matrix


print(pascal_triangle_app1(3))
print(pascal_triangle_app1(5))
