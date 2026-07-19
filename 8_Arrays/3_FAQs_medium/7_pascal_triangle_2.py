"""
- Given r, find all values of that row of pascal triangle and return it in array

Approach 1:
- Using the approach of nCr, we can find it, but TC is more
TC -> O(r*r) at worst
    - r iterations, since rth row has r elements
    - Each element we perform r iterations to find nCr

Approach 2:
    - Observe the nCr values for each element
    - Ex -> For r=6
        1 5 10 10 5 1
            1st and last column is 1
            For 2nd column:
                We need to find 5C1 -> 5/1
            For 3rd column:
                We need to find 5C2 -> 5*4/1*2
                    - Notice we already computed 5/1
                    - Extra is 4/2
            For 4th column:
                We need to find 5C3 -> 5*4*3/1*2*3
                    - Notice we already computed 5*4/1*2
                    - Extra is 3/3
            For 5th column:
                We need to find 5C4 -> 5*4*3*2/1*2*3*4
                    - Notice we already computed 5*4*3/1*2*3
                    - Extra is 2/4
        Observe the pattern of the extra term:
            -> r-c/c-1
        Initialy we keep prev = 1
        Then each term is:
            prev = prev*[(r-c)/(c)]

    - IMPORTANT CORRECTION
        - 1st element is always 1. So insert it to result array
        - And now run loop such that its 0-based indexing
        - From 1 to r-1, and apply this logic
        - The extra term now becomes
            r-c/c
        - Final update formula is
            prev = prev*[(r-c)/(c)]
            - Make sure this is done in 2 lines/steps
                prev = prev*(r-c)
                prev = prev //c
    - TC -> O(r)
"""


def ncr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle_row_app1(r):
    row = []
    for i in range(1, r + 1):
        if i == 1 or i == r:
            row.append(1)
        else:
            row.append(ncr(r - 1, i - 1))
    return row


def pascal_triangle_row_app2(r):
    row = [1]
    prev = 1
    for i in range(1, r):
        prev = prev * (r - i)
        prev = prev // i
        row.append(prev)
    return row


print(pascal_triangle_row_app1(4))
print(pascal_triangle_row_app2(4))
