"""
- Given integer, find its factorial

Approach:
- n=4
- 1*2*3*4
"""

def factorial(num):
    res = 1
    if num > 0:
        for i in range(1, num +1):
            res = res * i
    return res

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(4))
