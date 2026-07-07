"""
Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:
    - Every consecutive pair of integers have opposite signs.
    - For all integers with the same sign, the order in which they were present in nums is preserved.
    - The rearranged array begins with a positive integer

Approach 1:
    - We know how many elements are needed in result array
    - We also know positions
    - +ve ele -> 2i (until 2i < n)
    - -ve ele -> 2j+1 (until 2j < n)
    - This way we satisfy all conditions
    TC - create empty res array + put element in positions = n + n ==> O(2n)
    SC - O(n)

Approach 2:
    - So we can have 2 arrays, pos and neg
    - We can traverse main array and keep inserting the pos elements and neg elements
    - Now a final array which will be built taking ele from pos then ele from neg

    - TC -> O(n) + O(n/2) + O(n/2) === O(2n)
    - SC -> O(n/2) + O(n/2) + O(n)[If final array is new, else just put in original array] ==> O(2n) or O(n)

Why approach 1 is better ?
    - In approach 1, if you consider the creating result array part to be in constant time
    - TC is O(n), which is better than O(2n)
    - SC will still be O(n)

"""


def rearrange_by_sign_app1(nums):
    i, j = -1, -1
    n = len(nums)

    res = [0 for _ in range(0, n)]

    # Since we know + and - elements are equal we dont need to check if index crosses max range n
    for k in range(0, n):
        if nums[k] > 0:
            i += 1
            index = 2 * i
            res[index] = nums[k]
        elif nums[k] < 0:
            j += 1
            index = (2 * j) + 1
            res[index] = nums[k]

    return res


print(rearrange_by_sign_app1([2, 4, 5, -1, -3, -4]))
print(rearrange_by_sign_app1([1, -1, -3, -4, 2, 3]))
