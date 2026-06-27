"""
- Given an array os n integers, find the second highest occurring element.
- If multiple elements have same second highest frequency, return smallest element among them.

Approach:
    - Using brute force would give us O(nxn)
    - Again using the concept to build the occurrences hash table first.
    - This time with matching index [Just to make things easier]
    - TC ~ O(n) + O(max(nums)) + O(n) + O(max(nums))
    - SC -> O(max(nums))
"""

def second_highest_occurrences(nums, n):
    max_element = max(nums)

    occurrences_hash_table = [0 for _ in range(0,max_element+1)]

    for i in range(0, n):
        occurrences_hash_table[nums[i]] += 1

    highest_element = 0
    second_highest_element = -1

    for i in range(1, max_element+1):
        if occurrences_hash_table[i] > occurrences_hash_table[highest_element]:
            second_highest_element = highest_element
            highest_element = i
        elif occurrences_hash_table[i] < occurrences_hash_table[highest_element]:
            if occurrences_hash_table[i] > occurrences_hash_table[second_highest_element]:
                second_highest_element = i
    
    return second_highest_element

print(second_highest_occurrences([1,2,2,3,3,3],6))
print(second_highest_occurrences([4,4,5,5,6,7],6))
print(second_highest_occurrences([10,9,7,7],4))