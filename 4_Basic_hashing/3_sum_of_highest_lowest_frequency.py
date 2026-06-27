"""
- Given an array of n integers, must find the sum of highest frequency and lowest frequency.

Approach:
    - Using the concept of hashing.
    - Computing occurrences hashing and them finding lowest and highst frequency sum

    - TC ~ 2xO(n) + 2xO(max(nums))
    - SC -> O(max(nums))
"""

def highest_lowest_frequency(nums, n):
    max_ele = max(nums)
    occ_hash_table = [0 for _ in range(0, max_ele+1)]
    for i in range(0, n):
        occ_hash_table[nums[i]] += 1

    lowest_frq = 1
    highest_frq = 1

    # Coz given that array will have elements >= 1
    for i in range(1, max_ele+1):
        if occ_hash_table[i] > highest_frq:
            highest_frq = occ_hash_table[i]
        # Coz if its 0, its just there in hash table, not in array
        if occ_hash_table[i] != 0 and occ_hash_table[i] < lowest_frq:
            lowest_frq = occ_hash_table[i]
    
    return highest_frq + lowest_frq

print(highest_lowest_frequency([1,2,2,3,3,3],6))
print(highest_lowest_frequency([4,4,5,5,6],5))
