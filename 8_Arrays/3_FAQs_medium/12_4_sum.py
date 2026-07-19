"""
Problem:
    - Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
        a, b, c, d are all distinct valid indices of nums.
        nums[a] + nums[b] + nums[c] + nums[d] == target.
    - Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.

Brute force approach:
    - Vary each of the four possible values keeping others constant
    - 4 nested loops
    TC -> n^4 x nlogn to sort quadraple
        - O(n^4 x nlogn)
        - Too high
    SC - O(num quadruples)

Better approach:
    - Using three values, to find fourth
    - Using hashset to check if the fourth exists
    TC -> n^3 x nlogn
    SC -> O(hashset length) + O(num quads)*2

Optimal approach:
    - Sort array
    - Fix i and j
    - Vary k and l
    - Same logic as 3 sum, but kepping i and j ass constant and k and l as variable

    TC -> n^2 x n + nlogn ==> n^3 + nlogn ~ n^3
    SC -> O(num of quads)
"""


def brute_approach(nums, target):
    res = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        if temp not in res:
                            res.append(temp)

    return res


def better_approach(nums, target):
    res = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            map = {}
            for k in range(j + 1, n):
                more_needed = target - (nums[i] + nums[j] + nums[k])
                if more_needed in map:
                    temp = [more_needed, nums[i], nums[j], nums[k]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                map[nums[k]] = k
    return res


def optimal_approach(nums, target):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1

            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum > target:
                    l -= 1
                elif sum < target:
                    k += 1
                else:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return res


print(brute_approach([1, -2, 3, 5, 7, 9], 7))
print(brute_approach([7, -7, 1, 2, 14, 3], 9))
print(brute_approach([1, 1, 3, 4, -3], 5))

print(better_approach([1, -2, 3, 5, 7, 9], 7))
print(better_approach([7, -7, 1, 2, 14, 3], 9))
print(better_approach([1, 1, 3, 4, -3], 5))

print(optimal_approach([1, -2, 3, 5, 7, 9], 7))
print(optimal_approach([7, -7, 1, 2, 14, 3], 9))
print(optimal_approach([1, 1, 3, 4, -3], 5))
