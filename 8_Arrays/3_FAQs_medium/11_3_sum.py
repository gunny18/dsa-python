"""
- Given an array nums, find, i, j, k (all are different) such that nums[i]+nums[j]+nums[k]=0
- The triplets cannot be repeated
- Triplets of elements have to be returned

Brute Force Approach:
    - Iterate over all combinations of triplets -> n^3
    - Check if the values are 0 sum - 1
    - Sort each triplet and check if already present - 3log3
    TC = O(n^3 + nlogn)
    SC = O(num of triplets)

    PROBLEM ->> TLE

Better approach:
    - The main issue with brute force is the n^3 - 3 nested loops
    - We can try and reduce the 3rd loop k
    - We can first store a hash map of elements mapped to index
    - We have 2 loops of i and j to get 2 values
    - 3rd one can be calculated, and checked in hash map for existence.

    TC -> n^2 + nlogn + n = O(n^2 + nlogn + n)
    SC -> O(num triplets)

    PROBLEM ->> TLE

Optimal Solution: Three pointer approach
    - First sort the array
    - Take i at 0, j at i+1 and k at end
    - Three cases to handle.
        - sum > 0
            - Means, we need to decrease -> decrease k
        - sum < 0
            - Means, we need to increase -> increase j
        - sum = 0
            - Add the triplet
                - Triplet already in sorted order as elements are sorted
            - Move j to a location not same as curr j element
            - Move k to a location not same as current k element
    - The moment j >= k happens
        - Need to change i position -> We have checked all cases of triplets with static i
        - Change i to position not same as curr i element
        - Repeat process

    TC
        - nlogn + nxn (fixed i and j,k logic)
        - O(nlogn + n^2)
    SC
        O(num of triplets)

    CONCEPT:
        - Static i and variable j and k
        - Movement of i, j, k
"""


def brute_force_method(nums):
    n = len(nums)

    all_triplets = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = [nums[i], nums[j], nums[k]]
                    triplets.sort()
                    if triplets not in all_triplets:
                        all_triplets.append(triplets)

    return all_triplets


def better_approach(nums):
    all_res = []
    n = len(nums)

    for i in range(n):
        traversed_seconds = []
        for j in range(i + 1, n):
            third_ele = -(nums[i] + nums[j])
            if third_ele in traversed_seconds:
                temp = [nums[i], nums[j], third_ele]
                temp.sort()
                if temp not in all_res:
                    all_res.append(temp)
            traversed_seconds.append(nums[j])

    return all_res


def optimal_solution(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return res


print(brute_force_method([2, -2, 0, 3, -3, 5]))
print(better_approach([2, -2, 0, 3, -3, 5]))
print(optimal_solution([2, -2, 0, 3, -3, 5]))
