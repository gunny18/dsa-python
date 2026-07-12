"""
- Given a integer n check if its a perfect number
- An integer is a perfect number if sum of all its divisors (except the number itself) is same as the number
- We will always be given a integer >= 1

Approach 1:
- Say we have 28
- We loop until 1->27
- Check if divisions -> 0 remainder
- If so add them up
- Finally check the sum and the number
- TC -> O(n)
- SC -> O(1)


Approach 2:
- Say we have 36.
- 1*36 -> 36
- 2*18
- 3*12
- 4*9
- 6*6

- From all these if 1 is a divisor, then 36 is also a divisor, since 1*36 = 36.
- Similarly if 2 is a divisor then 18 is also a divisor.
- Untill 6.
- 6 is square root of 36
- So we can run a loop upto square root of the number
- At each step, in case we find a divisor, we can find a second divisor as well
- We can always keep 1 as a divisor since we are guaranteed to get a number > 1

- TC -> O(sqrt(n))
- SC -> O(1)
"""


def brute_force(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num


def optmised(num):
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum += i
            if i != (num / i):
                sum += num / i
        i += 1

    return sum == num


"""
- Same as above optimised version.
- Handles edge cases better, like n=1, is not a perfect number!
- Early exit if sum inside loop is already > number!
- Not adding perfect square root (16) devisor twice!
"""


def isPerfect(n: int) -> bool:
    i = 1
    divisor_sum = 0
    while i * i <= n:
        primary_divisor = n % i
        if primary_divisor == 0 and i != n:
            divisor_sum += i
            other_divisor = n // i
            if i != other_divisor and other_divisor != n:
                divisor_sum += other_divisor
        if divisor_sum > n:
            return False
        i += 1
    return divisor_sum == n


print(brute_force(28))
print(brute_force(36))
print(brute_force(12))

print(optmised(28))
print(optmised(36))
print(optmised(12))
print(optmised(1))
