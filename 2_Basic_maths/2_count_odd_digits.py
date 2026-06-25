"""
- Given a integer we need to find how many are odd digits

Approach:
- If num itself is 0 -> 0 is neither odd nor even, so does not count
- %10 to get each digit as remainder -> modulus
- Check if odd or even
- If odd increase count
- Else proceed to prev digit
- Repeat until num becomes 0
"""

def count_odd_digits(num):
    if num == 0:
        return 0
    odd_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 1:
            odd_count += 1
        num = num//10
    return odd_count


print(count_odd_digits(0))
print(count_odd_digits(1234567))
print(count_odd_digits(2468))
print(count_odd_digits(2233331))
