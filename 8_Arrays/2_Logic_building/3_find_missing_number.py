"""
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

Approach 1:
    - Use occurence hash map
    TC -> O(n) [build hash table] + O(n) [iterate hash table]
    SC -> O(n) -> hash table

Approach 2:
    Using sum of n numbers formula. Since the elements are distinct
    1. Given array of size n, find sum -> n(n+1)/2
    2. Now calculate actual sum
    3. If total = actual -> 0 is missing.
        If actual < total -> total - actual is the missing number
    Either ways return total - actual
    
    TC -> O(n) to calculate sum
    SC -> O(1)

Approach 3: XOR
    Concept of XOR
        -> 0 ^ a => a
        -> a ^ a => 0
    Ex -> [0,2,3,1,4]
    Xor1 -> 0^2^3^1^4 (Xor of given numbers)
    Xor2 -> 0^1^2^3^4^5 (Xor of 0 to n)
    Missing number = Xor1 ^ Xor2
        - From Xor1 ^ Xor2, many things cancel out
        - So 0^0, 1^1, 2^2, 3^3, 4^4, ^5
        - We get 0 ^ 5 => 5
    
    TC -> O(n)
    SC -> O(1)

    Why is this better than sum of natural numbers approach ?
        - For large n value, we need to find sum, which will be > n
        - So we need bigger memory to store large sums
        - XOR of large values will still never cross the large n itself
        - Hence slightly better
"""

def find_missing_number_1(nums):
    n = len(nums)
    total_sum = (n*(n+1))//2
    # Can use loop alsi, will still take the same O(n) to find sum
    actual_sum = sum(nums) 
    
    return total_sum - actual_sum

def find_missing_number_2(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(0, n):
        xor1 = xor1 ^ nums[i]
        xor2 = xor2 ^ i
    # xor2 still needs to be ^ with the last number n
    xor2 = xor2 ^ n
    return xor1 ^ xor2

print(find_missing_number_1([0,2,3,1,4]))
print(find_missing_number_1([0,2,1,4,5,6]))
print(find_missing_number_1([0]))
print(find_missing_number_1([1,2,3]))

print(find_missing_number_2([0,2,3,1,4]))
print(find_missing_number_2([0,2,1,4,5,6]))
print(find_missing_number_2([0]))
print(find_missing_number_2([1,2,3]))