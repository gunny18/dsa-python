"""
- Given an array of size n, return count of number of odd numbers

Approach:
    - Traverse array, at each step check if number is odd
    - Return count
    - TC -> O(n)
    - SC -> O(1)
"""

def count_odd(arr, n):
    odd_count = 0
    for i in range(0,n):
        if arr[i]%2==1:
            odd_count += 1
    return odd_count

print(count_odd([1,2,3,4],4))
print(count_odd([1,2,3,3,9,7],6))