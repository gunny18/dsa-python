"""
- Given an array, check if its is sorted in non-decreasing order
"""

def check_sorted(nums, i):
    if i >= len(nums) - 1:
        return True
    
    if nums[i] > nums[i+1]:
        return False
    
    return check_sorted(nums, i+1)

print(check_sorted([1,2,3,4,5], 0))
print(check_sorted([1,6,3,4,5], 0))