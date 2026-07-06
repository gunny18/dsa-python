"""
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.
Return the number of unique elements in the array.

If the number of unique elements be k, then,
    - Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
    - The remaining elements, as well as the size of the array does not matter in terms of correctness.

Approach 1:
    - Using a hash table to store counts
    - Then from hash table return unique count and modify array as required
    TC -> O(n) + O(hash table)
    SC -> O(hash table)

Approach 2: Very similar to hash. ACTUALLY SAME AS APPROACH 1
    - Using temp array
    TC -> O(n) + O(temp)
    SC -> O(temp)

Approach 3:
    - Play with pointers
    - 0th index element is always going to be in non-duplicate array
    - So start j from 1
        - j indicates the index in nums where the next non-duplicate element must go to!
    - Iterate from 1 to n-1
        - Keep comparing nums[i] and nums[j-1]
        - If not same, make nums[j] -> nums[i]
        - Move j forward, to next location where non duplicate element must go to if exists!
    - Return j
        - j indicates the first j non duplicate/unique elements of nums
    TC
        - O(n) -> Single pass from 1 to n-1
    SC -> O(1)
"""

def remove_duplicates_from_sorted_array(nums):
    # At j = 0 we already have the first non duplicate element
    # j indicates where in nums the next non duplicate element goes
    j = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[j-1] != 0:
            nums[j] = nums[i]
            j += 1
    return j

print(remove_duplicates_from_sorted_array([0,0,3,3,5,6]))
print(remove_duplicates_from_sorted_array([-2, 2, 4, 4, 4, 4, 5, 5]))