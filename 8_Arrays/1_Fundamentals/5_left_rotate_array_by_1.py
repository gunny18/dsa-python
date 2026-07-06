"""
- Given an array, rotate array to the left by 1
Ex - [3,2,1,4,5] -> [2,1,4,5,3]

Observations:
    - This means, we need to move first element to last
    - Keep shifting others to left by 1 position

Approach 1:
    - Temporarily store 1st element.
    - Shift second element to left
    - Shift third element to left.
    - When last element is shifted
        - Put first element back there
    - Array is now rotated to left by 1
    TC -> Since we are shifting until last element
        ~ O(n)
    SC -> O(1)
        - Just temp variables
"""

def left_rotate_array_by_one_1(nums):
    n = len(nums)
    if n == 1:
        return nums
    i = 1
    first_ele = nums[0]
    while i < n:
        # Even if you dont replace with None, and keep it as it is, it works just fine!
        nums[i-1], nums[i] = nums[i], None
        if i == n-1:
            nums[i] = first_ele
        i += 1
    return nums

print(left_rotate_array_by_one_1([1,2,3,4,5]))
print(left_rotate_array_by_one_1([1,2]))
print(left_rotate_array_by_one_1([-11,2,3,4,19]))
