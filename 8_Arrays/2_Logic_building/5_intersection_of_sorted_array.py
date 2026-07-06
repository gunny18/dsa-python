"""
Approach 1: Hash table
    - Build hash table
    - The take only occurences that are common min(occ1, occ2) no of elements must be in result
    - TC
        - O(n1+n2) to find max
        - O(n1+n2) to initiate HT
        - O(n1+n2) to populate HT
        - O(max(nums1, nums2)) to build intersection
    - SC
        - O(max(n1, n2)) + O(max(nums1, nums2))
Approach 2: 2 pointer
    - Review the logic.
    - The thinking is right, but it got too complicated when the conditions where simple!
Approach 3: 2 pointer
    - Compare both, use the fact that it is sorted in ascending order
    - Compare both elements:
        If one of them lesser, move that fwd for compare
    - When equal, add to result
    - Ensures that each instance of element is mapped to another instance
    TC - O(n1 + n2)
    SC - O(max(n1, n2))
"""

def intersection_of_sorted_arrays_app2(nums1, nums2):
    i,j = 0,0
    n1, n2 = len(nums1), len(nums2)

    if n1 < n2:
        compare_arr = nums1
    else:
        compare_arr = nums2
    
    n = min(n1, n2)

    res = []

    while i < n and j < n:
        curr_ele_counter_nums1 = 0
        curr_ele_counter_nums2 = 0
        if n1 < n2:
            curr_ele = compare_arr[i]
        else:
            curr_ele = compare_arr[j]

        # nums1 counter
        if nums1[i] < curr_ele:
            i += 1
        elif nums1[i] == curr_ele:
            while i < n and nums1[i] == curr_ele:
                curr_ele_counter_nums1 += 1
                i += 1
        
        
        # nums2 counter
        if curr_ele_counter_nums1:
            if nums2[j] < curr_ele:
                j += 1
            elif nums2[j] == curr_ele:
                while j < n and nums2[j] == curr_ele:
                    curr_ele_counter_nums2 += 1
                    j += 1
        if curr_ele_counter_nums1 and curr_ele_counter_nums2:
            min_count = min(curr_ele_counter_nums1, curr_ele_counter_nums2)
            for _ in range(0,min_count):
                res.append(curr_ele)
    
    return res

def intersection_of_sorted_arrays_app3(nums1, nums2):
    i,j = 0,0
    res = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    
    return res
 
print(intersection_of_sorted_arrays_app2([1,2,2,3,5],[1,2,7]))
print(intersection_of_sorted_arrays_app2([1,2,2,3,3,3],[2,3,3,4,5,7]))
print(intersection_of_sorted_arrays_app2([-45,-45,0,0,2],[-50,-45,0,0,5,7]))

print(intersection_of_sorted_arrays_app3([1,2,2,3,5],[1,2,7]))
print(intersection_of_sorted_arrays_app3([1,2,2,3,3,3],[2,3,3,4,5,7]))
print(intersection_of_sorted_arrays_app3([-45,-45,0,0,2],[-50,-45,0,0,5,7]))