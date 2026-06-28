"""
- Given an array fund sum of array elements

Approach:
    - Again Head recursion makes sense
    - I need to move deeper into array
    - Aggregate while climbing back out

    - Here I have access only to array.
    - The function does not accept anything else
    - So during recursion I need to keep passing sections of array
    - At each step a smaller array
    - Until I get a empty array
        - This is the base condition
    - TC -> O(nxn)

In case:
    - The function also accepted another parameter we could use it as index to find sum in O(n)
"""

def sum_array(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_array(nums[1:])

def sum_array_2(nums, idx):
    if idx > len(nums) - 1:
        return 0
    return nums[idx] + sum_array_2(nums, idx + 1)

print(sum_array([1,2,3]))
print(sum_array([5,8,1]))

print(sum_array_2([1,2,3], 0))
print(sum_array_2([5,8,1], 0))