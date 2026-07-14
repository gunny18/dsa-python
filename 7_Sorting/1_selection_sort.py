"""
- Selection sort is an algorithm which can be used to order elements in a linear data structure.

Algorithm for array (Ascending order)
    - Find minimum element and its index
    - Swap first element with minimum element.
    - Do same steps for remaining portion of array.
    - At each step we incrmentally sort portions of the array

Example:
    - [13,46,24,52,20,9] -> n=6
    - Step 1:
        Min is 9, index 5
        Swap 13 and 9
        [9,46,24,52,20,13]
    - Setp 2 -> [9,13,24,52,20,46]
    - Setp 3 -> [9,13,20,52,24,46]
    - Setp 4 -> [9,13,20,24,52,46]
    - Setp 5 -> [9,13,20,24,46,52]

    - For n=6, array is sorted at 5 steps

Notes:
    - For array of size n, it requires maximum of n-1 steps to sort using selection sort algorithm
    - At each step finding the min index requires n-step units of time.
    - In total n + n-1 + n-2 +....
    - TC ~ O(nxn)
        For selection sort, this is the best, worst and avg TC
    - SC -> O(1) If we modify same array

"""


def find_min_element_index(nums, start_index):
    min_index = start_index
    for i in range(start_index, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i

    return min_index


def selection_sort(nums):
    n = len(nums)

    for step in range(0, n):
        min_index = find_min_element_index(nums, step)
        nums[step], nums[min_index] = nums[min_index], nums[step]

    return nums


print(selection_sort([13, 46, 24, 52, 20, 9]))
