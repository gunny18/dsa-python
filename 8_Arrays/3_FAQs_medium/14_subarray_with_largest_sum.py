"""
Given array nums, find subarray with largest sum, and return that largest subarray sum

Brute approach:
    - Iterating element by element
    - Find each sum of each subarray combination
    - Find max sum from the subarray sum array
    - Update the result largest sub array sum
    TC:
        i = 0 -> [n-1+n]
        i = 1 -> [n-2+n]
        ~ O(n^2)
    SC:
        -> O(n) at max to store subarray sum array

    TLE

Kadane's Algorithm:
    - Two variables -> sum and max_value
    - Iterate over each element
    - Increase sum by element value
    - Compare and Update max value if sum > max value
    - If sum < 0:
        Reset sum to 0
        Why:
            - Coz If sum has gine -ve, it means that next what you add to it, will have to diminish the negative
            effect, and then start positive addition
            - This way if next element is positive, that element is itself a subarray > sum!
    TC:
        O(n)
    SC:
        O(1)
"""


def brute_force_approach(nums):
    n = len(nums)
    final_sum = None
    for i in range(n):
        subarray_sum = [nums[i]]
        for j in range(i + 1, n):
            subarray_sum.append(subarray_sum[-1] + nums[j])
        max_subarray_sum = max(subarray_sum)
        if final_sum is None or max_subarray_sum > final_sum:
            final_sum = max_subarray_sum
    return final_sum


def kadanes_algorithm(nums):
    sum = 0
    max_value = None

    for num in nums:
        sum += num
        if max_value is None or sum > max_value:
            max_value = sum
        if sum < 0:
            sum = 0

    return max_value


def kadanes_algorithm_to_find_subarray(nums):
    sum = 0
    max_value = None

    start_index = -1
    end_index = -1

    for i in range(len(nums)):
        sum += nums[i]
        if max_value is None or sum > max_value:
            max_value = sum
            if start_index == -1:
                start_index = i
            end_index = i
        if sum < 0:
            start_index = i
            sum = 0

    return nums[start_index : end_index + 1]


print(brute_force_approach([2, 3, 5, -2, 7, -4]))
print(kadanes_algorithm([2, 3, 5, -2, 7, -4]))
print(kadanes_algorithm_to_find_subarray([2, 3, 5, -2, 7, -4]))
