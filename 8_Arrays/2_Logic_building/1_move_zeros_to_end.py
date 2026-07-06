"""
- Given an array, push all 0s to the end
- Relative order of other elements must be maintained

Approach 1:
    - Using concept of left rotate
    - Find consecutive 0s to left rotate
    - When encountered a non zero element, perform the left rotate by k operation.
    - Proceed until end
    TC:
        - O(n) -> Traversinf entire array
        - When consecutive 0 in encountered, left rotate -> [O(n-start index of non zero) + O(no of consecutive 0s)]
            - Performed ===> No of times consecutive 0s are encountered before non zero
    SC -> O(1)
        - No extra space!
    
    TLE:
        - For larger n we get TLE issues!

Approach 2: 2 pointer approach
    - j -> Always points to 0 element index
    - i -> starts from j+1
    - Check if nums[i] is non zero
        - Yes
            - Swap nums[i] and nums[j]
            - Increment i and j
        - No
            - Increment i
    - TC -> O(x) -> x = first 0 element index
        -> O(n-x)
        =====> O(n)
    - SC -> O(1)
"""

def left_rotate_by_k(nums, k, start):
    n = len(nums)
    # Shift other elements to left by k
    for i in range(start, n):
        nums[i-k] = nums[i]
    # In sert 0s
    for i in range(n-k, n):
        nums[i] = 0

def move_zeros_to_end_1(nums):
    i = 0
    count = 0
    n = len(nums)
    while i < n:
        if nums[i] == 0:
            count += 1
            i += 1
        else:
            if count > 0:
                left_rotate_by_k(nums, count, i)
                # Edge case
                i -= count
                count = 0
            else:
                # Edge case
                i += 1
    return nums
    
def move_zeros_to_end_2(nums):
    n = len(nums)
    j = None
    # Find 1st 0 element index
    for i in range(0, n):
        if nums[i] == 0:
            j = i
            break
    
    # Start swaps logic
    # Handle case where there is no 0s in array
    if j is not None:
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
    
    return nums
    

print(move_zeros_to_end_1([0,0,0,1,3,-2]))
print(move_zeros_to_end_1([0,1,4,0,5,2]))
print(move_zeros_to_end_1([11,0,90,0,-51,-10,-1]))

print(move_zeros_to_end_2([0,0,0,1,3,-2]))
print(move_zeros_to_end_2([0,1,4,0,5,2]))
print(move_zeros_to_end_2([11,0,90,0,-51,-10,-1]))