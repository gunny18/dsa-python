"""
Approach 1: Hash table
    - Build hash table of occurences
    - Traverse hash table and build the resultant array
    - TC
        O(n1+n2) -> Initialize hash table
        O(n1 + n2) -> Populate hash table
        O(n1 + n2) -> Final union arrray
    - SC -> O(n1 + n2) + O(n1 + n2)

Approach 2: 2 pointer
    - Goal is to build this array in a single pass of both nums1 and nums2
    - Compare both until possible and insert to res, until one of the array is traversed
        - Also check if last element in result is same as the one being compared
    - Remaining elements of nums1 insert to res
        - Also check if last element in result is same as the one being compared
    - Remaining elements of nums2 insert to res
        - Also check if last element in result is same as the one being compared
    - TC -> O(n1+n2)
    - SC -> O(n1+n2)

Approach 3: Set
    - We can also use the concept of set
    - Iterate nums1, insert all (Set handles uniqueness part)
        - O(n1logn1)
    - Same for nums2
    - Iterate set and create result array
    - TC -> O(n1logn1) + O(n2logn2) + O(n1+n2)
    - SC -> O(n1+n2) + O(n1+n2)
"""

def union_of_2_sorted_array_app1(nums1, nums2):
    i = 0
    j = 0

    n1 = len(nums1)
    n2 = len(nums2)

    res = []
    
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            if (len(res) == 0 or res[-1] != nums1[i]):
                res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            if (len(res) == 0 or res[-1] != nums1[i]):
                res.append(nums1[i])    
            i += 1
        elif nums1[i] > nums2[j]:
            if (len(res) == 0 or res[-1] != nums2[j]):
                res.append(nums2[j])
            j += 1
    
    while i < n1:
        if (len(res) == 0 or res[-1] != nums1[i]):
            res.append(nums1[i])
        i += 1

    while j < n2:
        if (len(res) == 0 or res[-1] != nums2[j]):
            res.append(nums2[j])
        j += 1
    
    return res

print(union_of_2_sorted_array_app1([1,2,3,4,5],[1,2,7]))
