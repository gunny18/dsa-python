"""
- Given an array, reverse it. Using recursion

Approach:
    - Using two pointer with head recursion
"""


def reverse_array(nums, start, end):
    if start >= end:
        return
    
    nums[start], nums[end] = nums[end], nums[start]
    reverse_array(nums, start+1, end-1)

nums = [1,2,3,4,5]

reverse_array(nums, 0, len(nums)-1)
print(nums)