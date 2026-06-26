"""
- Given integer, find largest digit
"""

def largest_digit(num):
    largest = 0
    while num > 0:
        last_digit = num % 10
        if last_digit > largest:
            largest = last_digit
        num = num // 10
    return largest


print(largest_digit(121))
print(largest_digit(0))
print(largest_digit(121231))
print(largest_digit(21112))
