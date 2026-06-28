"""
- Given a number (integer), find sum of its digits repeatedly, until its a single digit number

Ex - 356
    - Sum = 14
    - Sum = 5 -> Single digit, so return
"""

def sum_digits(num):
    if num < 10:
        return num
    
    sum = 0
    while num != 0:
        sum = sum + (num % 10)
        num = num // 10
    
    return sum_digits(sum)

print(sum_digits(529))