"""
- Given a number check if its prime

Approach
    - Can check upto sqrt of number, if any divisors exist
"""

def check_prime(n, i):
    if n == 1:
        return False
    if i*i > n:
        return True
    
    if n % i == 0:
        return False
    return check_prime(n, i + 1)


print(check_prime(3, 2))
print(check_prime(5, 2))
print(check_prime(15, 2))