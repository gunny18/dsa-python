"""
- Given an array of size n, check if it is sorted in ascending/increasing/non-decreasing order.

Approach:
    - Condition is arr[0] <= arr[1] <= arr[2] ..... <= arr[n-1]
    - Traverse array, check for false condition where array will not satisfy above
    - Check arr[i] > arr[i+1]
        - If so stop traversing, return False
    - Else continue for all elements comparison.
    - TC -> O(n-1) -> O(n)
    - SC -> O(1)
"""

def check_sorted_ascending(arr, n):
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(check_sorted_ascending([1,2,3,4],4))
print(check_sorted_ascending([1,2,6,4,3,5],6))