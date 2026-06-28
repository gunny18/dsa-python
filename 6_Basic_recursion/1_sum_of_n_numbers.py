"""
- Given integer n, return sum of first n natural numbers. Use recursion

Approach:
    - N = 4
    - 1+2+3+4 = 10
    - I start with 4

    - Head recursion
        - Go until 0, return 0 (Base Cond)
        - Then do 1+0
        - Then 2+[1+0]
        - Then 3+[2+[1+0]]
        - The 4+[3+[2+[1+0]]]
            - This was the first call
            - this is returned!
"""

def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n-1)

print(sum_of_n(4))