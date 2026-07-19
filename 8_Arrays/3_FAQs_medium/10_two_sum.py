"""
- Given an array of integers and a target, return indexes of 2 elements, which add up to the target
- It says only one valid index pair exisits to get the target

Brute force approach:
    - For each element in array, add every other element until we get target
    TC -> O(n^2)
    SC -> O(1)

Better solution: -> This is still an optimal solution!
    - Using hashing concepts
    - Build hash map to store existence of a number
    - Then for each element, check if the other number exists to reach target!
    - TC -> n + logn => O(nlogn)
        - Depending on data structure used for hashing, it can be nlogn, n^2 or n!
    - SC -> O(n)

Optimal Solution:
    - Involves sorting
    - Sort the given array
    - Then use 2 pointer approach
        - nums[left] + nums[right] > target
            - Means we need to reduce operands
            - Reduce -> Decrement right
        - nums[left] + nums[right] < target
            - Means we need to increase operands
            - Increase -> Increment left
    - TC -> nlogn + n ==> O(n+nlogn) ~~ O(nlogn)
    - SC -> O(1)
    PROBLEM:
        - This will change indexes in array!
"""


def brute_force_approach(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]
    # In case no such index pair exists
    return [-1, -1]


def better_approach(nums, target):
    map = {}

    for i in range(len(nums)):
        more_needed = target - nums[i]
        if more_needed in map:
            return [map[more_needed], i]
        map[nums[i]] = i

    return [-1, -1]


def optimal_solution(nums, target):
    extended_pairs = []

    for i in range(len(nums)):
        extended_pairs.append([nums[i], i])

    extended_pairs.sort(key=lambda x: x[0])

    left = 0
    right = len(extended_pairs) - 1

    while left < right:
        sum = extended_pairs[left][0] + extended_pairs[right][0]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [extended_pairs[left][1], extended_pairs[right][1]]

    return [-1, -1]


print(brute_force_approach([1, 6, 2, 10, 3], 7))
print(brute_force_approach([1, 3, 5, -7, 6, -3], 0))

print(better_approach([1, 6, 2, 10, 3], 7))
print(better_approach([1, 3, 5, -7, 6, -3], 0))

print(optimal_solution([1, 6, 2, 10, 3], 7))
print(optimal_solution([1, 3, 5, -7, 6, -3], 0))
