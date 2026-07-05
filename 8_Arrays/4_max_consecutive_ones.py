"""
- Given an array if 0s and 1s, find maximum number of consecutive ones

Approach 1:
    - Build a hashtable to store the counts of consecutive 1s
    - Iterate hashmap to find the maximum value
    - TC
        - Build hash table -> O(n) as it has to be built by iterating over entire array
        - Iterate over hash table -> O(num consecutive 1s instances)
        ~ O(n) + O(num consecutive 1s instances)
    - SC
        - O(num consecutive 1s instances) -> Space taken to store hash table

Approach 2: No hash table
    - Same as 1, but trying to make it efficient in terms of space.
    - Just have 1 variable max_count.
    - A loop wise variable, current_max_count
    - We can just increment max_count, if current_max_count > max_count
    - This way we no need to have additional TC to find max value from hash table
    - This eliminates need for such a hashtable

    - TC -> ~ O(n)
        - Additional TC to find max is removed
    - SC -> O(1)
        - No additional hash table space
"""


def count_max_consecutive_ones_1(nums):
    consectuive_ones_hash = []
    consecutive_couter = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            i += 1
        else:
            while i < len(nums) and nums[i] == 1:
                consecutive_couter += 1
                i += 1
            if consecutive_couter != 0:
                consectuive_ones_hash.append(consecutive_couter)
                consecutive_couter = 0
    if len(consectuive_ones_hash) != 0:
        return max(consectuive_ones_hash)
    return 0

def count_max_consecutive_ones_2(nums):
    max_count = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            i += 1
        else:
            local_count = 0
            while i < len(nums) and nums[i] == 1:
                local_count += 1
                i += 1
            if local_count != 0 and local_count > max_count:
                max_count = local_count
    return max_count
            
print(count_max_consecutive_ones_1([1,1,0,0,1,1,1,0]))
print(count_max_consecutive_ones_1([0,0,0,0,0,0,0]))
print(count_max_consecutive_ones_1([1,0,1,1,1,0,1,1,1]))

print(count_max_consecutive_ones_2([1,1,0,0,1,1,1,0]))
print(count_max_consecutive_ones_2([0,0,0,0,0,0,0]))
print(count_max_consecutive_ones_2([1,0,1,1,1,0,1,1,1]))