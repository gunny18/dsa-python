"""
- Given a integer we need to reverse the number

Approach:
- rev number = 0
- Get last digit by num % 10
- rev number = rev number * 10 + last digit
- Repeat until number is 0

Approach 2:
- If we could string contanate it, we could just use this to type cast and concatenate to form the reversed number.
"""

def reverse_digits(num):
    rev_num = 0
    while num != 0:
        last_digit = num % 10
        rev_num = rev_num * 10 + last_digit
        num = num // 10
    return rev_num

if __name__ == "__main__":
    print(reverse_digits(0))
    print(reverse_digits(1234567))
    print(reverse_digits(2468))
    print(reverse_digits(2233331))
