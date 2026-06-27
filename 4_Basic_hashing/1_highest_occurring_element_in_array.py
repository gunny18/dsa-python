"""
- Given array of n integers, find element with most frequency (highest occurrences)
- If multiple elements have same frequence, return the smallest among those numbers

Approach:
    - I could just write a function to find occurrences 1 element at a time.
    - Again the TC issue comes -> TC -> O(nxn)
    - So lets pre compute all occurrences once and then use that in the algorithm
    - Steps
        - Build number occurrences hash table -> O(n)
            - First need to find max element in array
            - Or assume a large array
            - I prefer the finding max solution, though this will take extra TC now -> O(n)
        - Iterate over array and fetch occurrences from hash table -> O(n x 1)
            - Compare and find solution acc to given conditions in problem
    - TC -> O(n) + O(max(nums)) + O(n) + O(max(nums)) -> O(n) + O(max(nums)) << O(nxn)
    - SC -> O(max(nums))

    NOTE:
        - If needed though array is 0 index based, take extra size array to ensure number occurences is stored at that number index
        - in hash table
        - Avoids additional hash index and element/number computation confusions
"""

def highest_occurring(nums, n):
    # 1. Build hash table
    max_element = max(nums)
    occurrences_hash = [0 for _ in range(0, max_element)]
    # Hash index = element - 1
    for i in range(0, n):
        hash_index = nums[i] - 1
        occurrences_hash[hash_index] += 1
    
    # 2. Traverse hash table
    highest_occurring_element = 0
    for i in range(1, max_element):
        # Ensures in case of same frequency, lowest value is returned
        # As hash is stored in sorted order of elements.
        if occurrences_hash[i] > occurrences_hash[highest_occurring_element]:
            highest_occurring_element = i
    
    # Since hash index was calculated as element - 1
    return highest_occurring_element + 1

print(highest_occurring([1,2,2,3,3,3],6))
print(highest_occurring([4,4,5,5,6],5))
print(highest_occurring([2,4,3,2,5,4],6))