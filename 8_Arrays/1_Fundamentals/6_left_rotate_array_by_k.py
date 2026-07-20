"""
- Given an array, rotate array to the left by k places
Ex - [1,2,3,4,5,6], k=2
    Rotate left 1 place -> [2,3,4,5,6,1]
    Rotate left 2 place -> [3,4,5,6,1,2]

Observations:
    - This means, we need to move first element to last
    - Keep shifting others to left by 1 position
    - We need to do this for k times/steps

Approach 1:
    - Temporarily store 1st element.
    - Shift second element to left
    - Shift third element to left.
    - When last element is shifted
        - Put first element back there
    - Array is now rotated to left by 1
    - Repeat process for k times/steps
    TC -> Since we are shifting until last element, and doing it for k steps
        ~ O(kxn)
        - Max k can be n-1
        - So TC --> O(nxn-1) ==> O(n^2)
    SC -> O(1)
        - Just temp variables

    TLE Issues:
        - Gives TLE exceeded errors for large n and k value!

Approach 2:
    Ex -> [1,2,3,4,5,6], k=2
    No of rotations d = k % n
        - Imagine a case where k = 6. n = 6. So after 6, it will be same as org array.
        - This is how we tackle the TLE issue.
        - We dont need to shift always for given k
    - First copy the elements upto d in a temp array
        - temp -> [1,2]
    - Now we need to shift remaining elements, each by d places, starting at d
        - i = 2 (since d = 2)
            - Shift nums[2] to nums[0]
        - Shift nums[3] to nums[1].
        - Shift nums[i] to nums[i-d]
    - Now put the temp elements back
        - Start from n-d
        - i = 4 (n=6, d=2)
        - Put temp[0] in nums[4]
        - temp[1] in nums[5]
        - temp[i-(n-d)] = nums[i]

    TC:
        - O(d) temp array
        - O(n-d) shift remaining array each by d places
        - O(d) need to put back d elements from temp array
        ~ O(d+n-d+d) ===== O(n+d)
    SC -> O(d) -> Space to store temo d elements

Approach 3: By reversals
    Ex -> [1,2,3,4,5,6], k=2
    - Find effective shifts
        k = k % n
    - We have left array: [1,2] (Upto k=2)
        - Reverse it -> [2,1]
    - Right Array: [3,4,5,6]
        - Reverse it [6,5,4,3]
    - Combined array is
        - [2,1,6,5,4,3]
        - Reverse this -> [3,4,5,6,2,1]
        - This is the same array as left rotations by k!!!
    Algorithms (In place reversals)
        - Reverse(arr, 0, 0+d-1) -> O(d)
        - Reverse(arr, d, n-1) -> O(n-d)
        - Reverse(arr, 0, n-1) -> O(n)
    TC -> O(d+n-d+n) ===== O(2n)
        - Slightly increased from last approach!!!!
        - But this is balanced as now SC is O(1)
    SC -> O(1)
        - No temp array!
"""


def left_rotate_array_by_k_1(nums, k):
    n = len(nums)
    if n == 1:
        return nums
    while k > 0:
        i = 1
        first_ele = nums[0]
        while i < n:
            nums[i - 1] = nums[i]
            if i == n - 1:
                nums[i] = first_ele
            i += 1
        k -= 1
    return nums


def left_rotate_array_by_k_2(nums, k):
    n = len(nums)
    if n == 1:
        return nums
    # Effective no of left rotates
    k = k % n
    # temp array
    temp = [nums[i] for i in range(0, k)]
    # Shift remaining elements by k places each
    for i in range(k, n):
        nums[i - k] = nums[i]
    # Place back k temp elements
    for i in range(n - k, n):
        nums[i] = temp[i - (n - k)]

    return nums


def reverse_array(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def left_rotate_by_k_using_reversals(nums, k):
    n = len(nums)
    if n == 1:
        return nums
    # Effective no of left rotates
    k = k % n
    # Reverse d elements
    reverse_array(nums, 0, k - 1)
    # Reverse remaining array
    reverse_array(nums, k, n - 1)
    # Reverse complete array
    reverse_array(nums, 0, n - 1)
    # return nums
    return nums


print(left_rotate_array_by_k_1([1, 2, 3, 4, 5, 6], 2))
print(left_rotate_array_by_k_1([1], 2))
print(left_rotate_array_by_k_1([1, 2], 1))
print(left_rotate_array_by_k_1([1, 2], 2))

print(left_rotate_array_by_k_2([1, 2, 3, 4, 5, 6], k=2))

print(left_rotate_by_k_using_reversals([1, 2, 3, 4, 5, 6], k=2))
