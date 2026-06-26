"""
- Given a integer, it is a palindrome if the reversed number is same as the original number.

Approach 1:
- Find reverse of number
- Check if equal and decide if plaindrome
"""

def reverse_digits(num):
    rev_num = 0
    while num != 0:
        last_digit = num % 10
        rev_num = rev_num * 10 + last_digit
        num = num // 10
    return rev_num

def check_palindrome(num):
    rev = reverse_digits(num)
    return rev == num


print(check_palindrome(121))
print(check_palindrome(0))
print(check_palindrome(121231))
print(check_palindrome(21112))
