"""
Need for merge sort:
    - Previous sorting algorithms all take TC O(nxn)
    - That was the best, worst and avg TC
    - Merge sprt provides a way to improve that
Algorithm:
    - Divde and merge
        - Divide array into left and right array
        - Divide left array (Recursive)
        - Divide right array (recursive)
        - Merge the left and right array in sorted fashion
    
Analogy:
    - Completely divide left side
    - Completely divide right side
    - Then merge both and keep going up

Difference between approach 1 and 2:
    - The merge algorithm of left and right sorted array

Issues:
    - Needs a lot of Additional SC.
    - As we are passing new array after division
    - What if we can just pass the start and end index, instead of actually dividing the array
    - Logical division ?

Algorithm 3:
    - Modifies in place
    - Extra space only while merging to store temp merge sorted elements
    - We only logically divide elements
    - Even after merge they are put back in the sorted order in original array

TC ->
    - At each step the recursion tree has depth of logn
    - And we have height of tree as n
    - TC -> O(nlogn) <<< O(nxn)

SC -> O(temp array) + O(Auxiliary stack space)
"""

import math

def find_min_element_index(nums, start_index):
    min_index = start_index
    for i in range(start_index, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    
    return min_index

def merge_sort(nums):
    n = len(nums)
    if n == 1:
        # Reached bottom -> Single element array
        return nums
    # Divide left and right
    left = math.ceil(n/2)
    # Perform merge soft left
    left_sorted_array = merge_sort(nums[:left])
    # Perform merge sort right
    right_sorted_array = merge_sort(nums[left:])
    # Perform combined merge sort
    sorted_array = [0 for _ in range(0, len(left_sorted_array) + len(right_sorted_array))]
    for i in range(0, len(sorted_array)):
        if len(left_sorted_array) != 0 and len(right_sorted_array) != 0:
            left_min_index = find_min_element_index(left_sorted_array,0)
            right_min_index = find_min_element_index(right_sorted_array,0)
            if left_sorted_array[left_min_index] <= right_sorted_array[right_min_index]:
                sorted_array[i] = left_sorted_array[left_min_index]
                left_sorted_array.pop(left_min_index)
            else:
                sorted_array[i] = right_sorted_array[right_min_index]
                right_sorted_array.pop(right_min_index)
        elif len(left_sorted_array) != 0:
            left_min_index = find_min_element_index(left_sorted_array,0)
            sorted_array[i] = left_sorted_array[left_min_index]
            left_sorted_array.pop(left_min_index)
        elif len(right_sorted_array) != 0:
            right_min_index = find_min_element_index(right_sorted_array,0)
            sorted_array[i] = right_sorted_array[right_min_index]
            right_sorted_array.pop(right_min_index)
    return sorted_array

def merge_sort_2(nums):
    n = len(nums)
    if n == 1:
        # Reached bottom -> Single element array
        return nums
    # Divide left and right
    left = math.ceil(n/2)
    # Perform merge soft left
    left_sorted_array = merge_sort(nums[:left])
    # Perform merge sort right
    right_sorted_array = merge_sort(nums[left:])
    # Perform combined merge sort
    sorted_array = [0 for _ in range(0, len(left_sorted_array) + len(right_sorted_array))]
    left_ptr = 0
    right_ptr = 0
    # Compare from left and right
    i = 0
    while left_ptr < len(left_sorted_array) or right_ptr < len(right_sorted_array):
        if left_ptr < len(left_sorted_array) and right_ptr < len(right_sorted_array):
            if left_sorted_array[left_ptr] <= right_sorted_array[right_ptr]:
                sorted_array[i] = left_sorted_array[left_ptr]
                left_ptr += 1
            else:
                sorted_array[i] = right_sorted_array[right_ptr]
                right_ptr += 1
        elif left_ptr < len(left_sorted_array):
            sorted_array[i] = left_sorted_array[left_ptr]
            left_ptr += 1
        elif right_ptr < len(right_sorted_array):
            sorted_array[i] = right_sorted_array[right_ptr]
            right_ptr += 1
        i += 1
        
    return sorted_array

# Splitting divide and merge and performing it in place instead of new arrays at each step
def merge_array(nums, start, mid, end):
    temp = []
    # Need to merge [start....mid] [mid+1.....end]
    left = start
    right = mid+1

    while left <= mid and right <= end:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    
    while left <= mid:
        temp.append(nums[left])
        left += 1
    
    while right <= end:
        temp.append(nums[right])
        right += 1
    
    # Put these sorted range elements back into nums
    for i in range(start, end+1):
        # i-start becase we have sorted only the range start to high.
        # So in actual array need to replace only those
        nums[i] = temp[i-start]

def merge_sort_3(nums, start, end):
    if start >= end:
        # Reached bottom -> Single element array
        return nums
    # Divide left and right
    # IMPPPPP -> If we just calc mid using (end-start)//2 we get recursion error in case mid goes less than start
    mid = start + ((end-start)//2)
    # Perform merge soft left
    merge_sort_3(nums, start, mid)
    # Perform merge sort right
    merge_sort_3(nums, mid+1, end)
    # Perform combined merge sort
    merge_array(nums, start, mid, end)

    return nums
    

nums = [3,1,2,4,1,5,2,6,4]

print(merge_sort(nums))
print(merge_sort_2(nums))

print(merge_sort_3(nums,0,len(nums)-1))
        
            
