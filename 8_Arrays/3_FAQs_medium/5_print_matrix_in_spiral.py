"""
- For this, there is just single solution, nothing else.
- There is not brute, better, optimal, this is the only way to solve it

- Need to traverse in spiral
- Intuition is to ensure ig goes right, then down, then left, then up
    - Outer layer, inner layer, ......

Edge Cases
    - [[.....]] -> Only 1 row in matrix ---> 1xm case
    - [[a],[b],[c],..] -> Only one col in matrix ------> nx1 case
    These must be handled!!!!!

- TC -> O(mxn) ---> Need to go through every element once
- SC -> O(mxn) ----> To store spiral order elements
"""


def print_in_spiral(matrix):
    n = len(matrix)
    m = len(matrix[0])

    top, bottom = 0, n - 1
    left, right = 0, m - 1

    spiral = []

    while top <= bottom and left <= right:
        # Move right
        for i in range(left, right + 1):
            spiral.append(matrix[top][i])
        top += 1

        # Move down
        for i in range(top, bottom + 1):
            spiral.append(matrix[i][right])
        right -= 1

        # Move left
        if top <= bottom:  # Edge case for [[1,2,3]]
            for i in range(right, left - 1, -1):
                spiral.append(matrix[bottom][i])
            bottom -= 1

        # Move top
        if left <= right:  # edge case for [[1],[2],[3]]
            for i in range(bottom, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

    return spiral


print(print_in_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
