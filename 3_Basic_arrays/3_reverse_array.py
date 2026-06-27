"""
- Given an array of size n, need to reverse the given array

Approach:
    - We know index goes from 0->n-1
    - Traverse backwards
    - Store each array element in new temp array
    - Now from temp, we need to put elements back to array
    - TC -> O(n + n) -> O(n)
    - SC -> O(n)
        - Additional n space needed to store reversed array

Approach:
- In place reverse approach - Two pointer approach:
    - Pointer at 0
    - Pointer at n-1
    - Swap elements
    - Move pointers in either directions
    - Until start pointer < end pointer
    - TC -> O(n/2) -> O(n)
        - TC turns out to be same for worst case, but on an average, we know we dont have to traverse entire array
    - SC -> O(1)
        - No additional space apart from already existing array
"""

def two_pointer_swap_reverse(arr, n):
    start = 0
    end = n-1
    while start < end:
        tmp = arr[end]
        arr[end] = arr[start]
        arr[start] = tmp

        start += 1
        end -= 1
    print(arr)

two_pointer_swap_reverse([1,2,3,4],4)
two_pointer_swap_reverse([1,2,3,4,5],5)