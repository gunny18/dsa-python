"""
- Given a number find factorial. Use recursion

Approach:
    - 0! = 1
    - 1! = 1
    - 2! = 1x2
    - 3! = 1x2x3
    - n! = 1x2x3x.....x(n-1)xn

    Head recursion:
        - Compute from base then move up and compute aggregated as you climb up
    Base cond:
        - if n==0 -> return 1
"""

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(2))
print(factorial(4))
print(factorial(6))
print(factorial(0))
print(factorial(1))
    