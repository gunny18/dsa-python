"""
- Pick up one element at a time, ensure it is in its correct position
Algorithm:
    Ex -> [13,46,24,52,20,9]
    Element 13:
        - Consider 13 by itself.
        - By itself, it is in the correct position
    Element 46:
        - Compared with 13, it is in correct position
    Element 24:
        - Compared with 13,46, It has to appear after 13
        - So swap with 46
        - [13,24,46,52,20,9]
    Element 52:
        - Compared with 13, 24, 46, It is in correct position
    Element 20:
        - Compared with elements before it, it has to appear after 13
        - Swap with 52 -> [13,24,46,20,52,9]
        - Swap with 46 -> [13,24,20,46,52,9]
        - Swap with 24 -> [13,20,24,46,52,9]
        - Swap until it reaches correct position
    Element 9:
        - It has to appear before 13:
        - Swap until it does to get
        [9,13,20,24,46,52]
    - Once done for all elements, it is sorted

TC Analysis:
    - Assume worst case that every element has to appear 1st.
    - Max no of swaps.
    - So 1 swap, 2 swap, 3 swap, ... n swap
    - 1+2+.....+n ~ O(nxn)
    - This is the best, worst and avg case TC
"""

def insertion_sort(nums):
    n = len(nums)
    for i in range(0, n):
        if i != 0:
            k = i
            while k!= 0 and nums[k] < nums[k-1]:
                nums[k], nums[k-1] = nums[k-1], nums[k]
                k -= 1
    return nums

print(insertion_sort([13,46,24,52,20,9]))