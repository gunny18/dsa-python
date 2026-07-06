"""
- Given an array of integers, find the integer target. Find the smallest index where target appears.
- Return that index. If not found, return -1

Approach 1:
    - Go through array, 1 element at a time.
    - find index of first ocurrence.
    - Return it
    - else return -1
    TC -> O(n)
    SC -> O(1)
"""

def linear_search_1(nums, target):
    for i in range(0, len(nums)):
        if target == nums[i]:
            return i
        
    return -1


print(linear_search_1([2,3,4,5,3],3))