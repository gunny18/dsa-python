"""
Algorithmic approach:
- Given a integer number with no leading 0's
- Dividing the number until number is 0
- No of time we divide by 10 is the no of digits in the number.
- This has to be an integer division.
- Obviously we need to check if number itself is 0
- TC -> O(digits)

Formula based
- No of digits = log10(num) + 1
- Logarithm is with base 10
- TC -> O(log10(num))
"""

def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

print(count_digits(0))
print(count_digits(1235))