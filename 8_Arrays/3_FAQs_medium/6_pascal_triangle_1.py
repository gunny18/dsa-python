"""
Pascal triangle:
    - Every row starts with 1 and ends with 1
    - 1st row has only 1 element, 2nd row 2, and so on.....
    - Element at (r,c) -> Internal element -> Which occurs from 3rd row
        - Always sum of elements directly on top of it
        - P(r,c) = P(r-1,c) + P(r-1,c-1)
    - If r=c or c=1, then value is 1

Approach: Recursive
    - The formula is an approach itself, the base condition being 1 cases!
    TLE for large r and c

Algorithmic Approach:
    - Formula for Combinations of n elements, taking r at a time is nCr
    - nCr = n!/(r! x (n-r)!)
    - To find r,c element in pascal triangle ====> (r-1)C(c-1)
    But if we use this formula directly we again get TLE as TC is O(n) + O(r) + O(n-r)

    Combinations shortcut:
        - 10C3 --> 10!/(3!x7!) =====> 10x9x8x7!/(3!x7!) ====> (10x9x8)/(1x2x3)
        - Observation:
            So we consider the r=3 -> Numerator has 3 terms, so does denominator
            Numerator has 10-0 x 10-1 x 10-2
            Denominator has 0+1 x 0+2 x 0+3

    TC -> O(r) ---> We run loop for 3 times and comput nCr
"""


def pascal_triangle_rc_element_recursive(r, c):
    if c == r or c == 1:
        return 1
    return pascal_triangle_rc_element_recursive(
        r - 1, c
    ) + pascal_triangle_rc_element_recursive(r - 1, c - 1)


def combination_ncr(n, r):
    res = 1
    for i in range(0, r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle_rc_combination_approach(r, c):
    return combination_ncr(r - 1, c - 1)


print(pascal_triangle_rc_element_recursive(4, 2))
print(pascal_triangle_rc_element_recursive(5, 3))
print(pascal_triangle_rc_element_recursive(1, 1))

print(pascal_triangle_rc_combination_approach(4, 2))
print(pascal_triangle_rc_combination_approach(5, 3))
print(pascal_triangle_rc_combination_approach(1, 1))
