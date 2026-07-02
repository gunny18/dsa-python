"""
- Given an array of integers nums, return the second largest element in the array. If it does not exist, return -1

Approach:
    - We follow a similar approach to finding largest, just keep track of second largest as well
    - Additional condition needed to update second largest
    - TC ~ O(n)
    - SC ~ O(1)

Approach:
    - Again we can sort it and directly start checking for the second element from the last 2nd element.
        - Imagine a case where all elements are same
        - You sort it -> O(nlogn)
        - Then ieterate from last trying to find 2nd largest -> O(n)
    - TC -> O(nlogn) + O(n) -> Merge/Quick sort
    - SC -> O(1) + Stack space
"""

def find_second_largest(nums):
    sec_lg = None
    n = len(nums)
    if n == 1:
        return -1
    lg = nums[0]

    for i in range(1, n):
        if nums[i] != lg:
            if nums[i] > lg:
                sec_lg = lg
                lg = nums[i]
            elif sec_lg is None or nums[i] > sec_lg:
                sec_lg = nums[i]
    
    if sec_lg is None:
        return -1
    return sec_lg

print(find_second_largest([8,8,7,5,6]))
print(find_second_largest([8,8,8,8]))
print(find_second_largest([1000,-10000]))
