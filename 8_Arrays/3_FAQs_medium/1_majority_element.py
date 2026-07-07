"""
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

Constraints:
    n == nums.length.
    1 <= n <= 10^5
    -10^4 <= nums[i] <= 10^4
    One value appears more than n/2 times.

Aprroach 1: Occurences hash approach
    - Find max ele
    - Initiate hash table
    - Populate occurences in hash table
    - Iterate and find guaranteed majority element
    TC
        - O(n) -> find max -> m
        - O(m) -> Initiate hash table
        - O(n) -> Populate occurences
        - O(m) -> Find majority element
    SC
        O(m)

    PROBLEM:
        - There are -ve numbers also, so how to handle them ????

Approach 2: Hash map, using the dicts to store the map i.e dict as a hash table for lookup
    - Dictionary insertions and lookups are O(1) on an average
    - Usually map insertions take O(nlogn).
    - Depends on the map implementation.
    - Here dict implementation makes it O(1)
    TC
        - O(n)
        - O(1) -> Dict insertion
        - O(1) -> Dict lookup
        ---> O(n)
    SC -> O(n) ===> Dict stores n unique elements at worst, but this is not exact because array is guaranteed to have a majority element
"""


def find_majority_app1(nums):
    n = len(nums)
    occ_map = {}
    for num in nums:
        if num not in occ_map:
            occ_map[num] = 0
        # increment occ counter
        occ_map[num] += 1
        # Check if already majority - Guaranteed that there is 1 majority element. So this case has to happen at some point!
        if occ_map[num] > n / 2:
            return num
    raise Exception("No majority element found!")


print(find_majority_app1([7, 0, 0, 1, 7, 7, 2, 7, 7]))
print(find_majority_app1([1, 1, 1, 2, 1, 2]))
print(find_majority_app1([-1, -1, -1, -1]))
print(find_majority_app1([0]))
