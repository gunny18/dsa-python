"""
- Given 2 integers n1 and n2, find its least common multiple (LCM)
- LCM is the lowes positie integer which is divisible by n1 and n2

Brute force Approach:
- Say we have 3,5.
- We know to find LCM, it has to start from 5 -> max(3,5). <5 cannot be multiple of 3 and 5.
- So we keep a loop running with values 1,2,3....
- Keep finding multiples, 5*1, 5*2, ....
- Each multiple check if divisible by 3 & 5.
- We will eventually get a value.

TC -> O(n1*n2)
SC -> O(1)

GCD and LCM:
- LCM = (n1*n2)/gcd(n1,n2)
- If we use euclidean algo for gcd
- TC -> O(log(min(n1,n2)))
- SC -> O(1)
"""

def brute_force(n1, n2):
    min_multiple = max(n1, n2)
    i = 1
    while True:
        multiple = min_multiple*i
        if multiple%n1 == 0 and multiple%n2 == 0:
            return multiple
        i += 1

def gcd_euclidean_2(n1, n2):
    while n1!=0 and n2!=0:
        if n1>n2:
            n1%=n2
        else:
            n2%=n1
    if n1==0:
        return n2
    return n1

def lcm(n1, n2):
    return (n1*n2)//gcd_euclidean_2(n1,n2)

        
    
print(brute_force(3,5))
print(brute_force(90,4))

print(lcm(3,5))
print(lcm(90,4))
