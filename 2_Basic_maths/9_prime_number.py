"""
- Given an integer, need to check if its a prime number.
- A number is prime if it has no divisors, except, itself and 1.
- 1 is not a prime number. It is a compond number

Approach 1 - Brute force
- Check if all numbers from 2 to n-1 is a divisor
- If any are, number is not prime
- TC -> O(n)
- SC -> O(1)

Approach 2:
- Same concept as finding sum of divisiors.
- We can check upto sqrt(n)
- If a divisor is found, we can find other divisor also
"""

def optimised(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

print(optimised(1))
print(optimised(3))
print(optimised(4))
print(optimised(8))
print(optimised(7))
print(optimised(13))