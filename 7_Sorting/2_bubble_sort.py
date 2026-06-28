"""
Algorithm:
    - Push the maximum element to last using adjacent swaps and comparisons.
    - Repeat until array is sorted

Example:
    [9,46,24,52,20,13]
    Step 1:
        - Compare 9 and 46. Max element already at right.
        - Compare 46, 24
            - Swap
            [9,24,46,52,20,13]
        - Compare 46, 52 -> Its fine
        - Compare 52, 20
            - [9,24,46,20,52,13]
        - Compare 52, 13
            - [9,24,46,20,13,52]
        - Now Largest element of array is at end
    Step 2: [Must get largest element to right] [Ignore 52 as it is sorted]
        - We start from 0th index again
        - Final array -> [9,24,20,13,46,52]
    Step 3:
        - Final Array -> [9,20,13,24,46,52]
    Step 4:
        - Final Array -> [9,20,13,24,46,52]
    Step 5:
        - Final Array -> [9,13,20,24,46,52]
    So for n-6, we needed 5 steps to perform buble sort

Notes:
    - For array of size n, we require n-1 steps to perform bubble sort
    - At each step we go from 0 to n-step to perform adjacent swaps

TC Analysis:
    At any step:
        n - step comparisons
    Total n-1 steps
    -> (n-1) x (n-step) ~ O(nxn)
    - This is the best, worst and avg TC
"""

def bubble_sort(nums):
    n = len(nums)

    for step in range(0, n):
        for i in range(0, n-step-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums
            
print(bubble_sort([9,46,24,52,20,13]))
