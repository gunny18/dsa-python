"""
- Given an integer check if its an armstrong number

Armstrong number
- Sum of digit to power number of digit = number
- Then its armstrong number
Ex:
n = 153
1^3 + 5^3 + 3^3
1+125+27 = 153
Hence n = 153 is an armstrong number

- 0 is an armstrong number!
"""

import math


def check_armstrong(num):
    if num == 0:
        return True
    num_digits = math.floor(math.log10(num) + 1)
    org_num = num
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit**num_digits
        if sum > org_num:
            return False
        num = num // 10
    return sum == org_num


print(check_armstrong(153))
print(check_armstrong(123))
print(check_armstrong(1223))
