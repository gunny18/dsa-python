"""
- Given a number, find the fibonacci sequence

Fibonacci sequence:
    - F(0) = 0
    - F(1) = 1
    - For n > 1
        - F(n) = F(n-1) + F(n-2)
"""

def fibonaaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonaaci(n-1) + fibonaaci(n-2)

print(fibonaaci(2))
print(fibonaaci(3))