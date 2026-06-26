"""
- Given 2 integers n1 and n2, find the GCD
- GCD is the largest positive number which divides n1 and n2 perfectly

Approach 1 - Brute force:
Ex - 20, 40
- Go from 2 -> 20
- 20 because >20 cannot be a divisor for 20 and 40
- Check if divisons are perfect for both, if so, that is the largest

- TC -> O(min(n1, n2))
- SC -> O(1)

Approach 2 - Brute force:
- Now instead of going forwards can we start from back
- Go from min(n1,n2) -> 2
- The first match is the greates/largest common divisor
- Still

- TC -> O(min(n1,n2))
- But on an average this will yield better results


Optimised Approach 1 - Euclidean Algorithm

- gcd(n1,n2) = gcd(n1-n2, n2), if n1 > n2
- This is a mathematical algorithm, where intuition is that n1-n2 will also be divisible by the gcd

Steps:
    - If n1 > n2, reduce n1 to n1-n2
    - else n2 to n2-n1
    - Untill any 1 is 0.
    - The other number is the GCD

Flaw in this algorithm:
- How much time until we get to a point where any number is 0 ?
- If numbers are 100,5 or worst, 100,1.
- We need to keep going from gcd(100,1) -> (99,1) -> (98,1) -> ..... -> (0,1)

Fixing this:
- Essentially what we need to do is do an operation to get to a point where n1 < n2 or n2 < n1.
- Say we have 100, 15
- Closest to 100 is 15 * 6 = 90
- We directly go to 10, 15
- Same as subtracting 15 from 100, 6 times to get there.
- We can get 100 % 15 = 10 -> Which is where we want to go
- We repeat this until any 1 number reaches 0

- TC -> O(log(min(n1,n2)))
- SC -> O(1)
"""

def brute_force_1(n1, n2):
    largest = 1
    for i in range(2, min(n1,n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            largest = i
    return largest

def brute_force_2(n1, n2):
    for i in range(min(n1,n2), 1,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1

def gcd_euclidean_1(n1, n2):
    while n1!=0 and n2!=0:
        if n1>n2:
            n1-=n2
        else:
            n2-=n1
    if n1==0:
        return n2
    return n1

def gcd_euclidean_2(n1, n2):
    while n1!=0 and n2!=0:
        if n1>n2:
            n1%=n2
        else:
            n2%=n1
    if n1==0:
        return n2
    return n1

print(brute_force_1(10,20))
print(brute_force_1(20,44))

print(brute_force_2(10,20))
print(brute_force_2(20,44))

print(gcd_euclidean_1(20,44))
print(gcd_euclidean_1(100,5))

print(gcd_euclidean_2(20,44))
print(gcd_euclidean_2(100,5))

