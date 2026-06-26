"""
- Given an integer we need to count number of prime numbers untill that number

Approach:
- Go from 2->n-1
- Check if each is a prime.
- If yes increment counter
- TC -> O(n*srt(n))
- SC -> O(1)
"""

def isPrime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def count_prime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    prime_counter = 0
    for i in range(2, num):
        if isPrime(i):
            prime_counter += 1
    return prime_counter

print(count_prime(10))
print(count_prime(2))
print(count_prime(1))
print(count_prime(6))