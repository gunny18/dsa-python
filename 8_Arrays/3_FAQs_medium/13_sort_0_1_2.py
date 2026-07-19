"""
Brute Force Approach:
    - Scan for 0, and store
    - Scan for 1 and store
    - Scan for 2 and store

    TC -> n + n -> O(2n) -> O(n)
    SC -> O(n)

Better Approach:
    - Hashmap
    - Store counts in hash map
    - Sort array as per counts

    TC -> n + 0,1,2 counts -> n -> O(2n) -> O(n)
    SC -> O(3) -> We need only 0,1,2 counts -> O(1)

Sorting approach:
    - Just sort array
    - TC -> O(nlogn)
    - SC -> Sorting internally needs space (stack), temp arrays etc, depending on sorting method used!

Counter Approach:
    - Counters for 0, 1, 2
    TC:
        n + n
        O(2n) -> O(n)
    SC -> O(1)

Dutch National Flag Algorithm:
    - Three pointers - low, mid and high
    Rules:
        1. 0 to low-1 will be 0s -> extreme left
        2. low to mid-1 will be 1
        3. high+1 to n-1 will be 2s -> extreme right

    NOTE -> mid to high ---> Unsorted portion on which we are trying to sort, based on above three rules

    Algorithm:
        - Initially my mid will be 0, high = n-1, since entire array is unsorted
        - low is also at 0, since logically speaking no elements is sorted.

        Now applying above rules in terms of a[mid]
            a[mid] = 0
                - We know this has to be within 0 to low-1
                - So we swap a[mid], a[low]
                    - low++
                    - mid++
            a[mid] = 1
                mid ++
            a[mid] = 2
                swap(a[mid], a[high])
                high--
        When mid goes past high -> mid > high
            - It means our unsorted portion has vanished
            - Meaning the unsorted portion are in their sorted portions as per the rules.

    TC -> O(n)
        - Just 1 traversal of the unsorted portion
    SC -> O(1)
"""


def brute_approach(nums):
    temp = []
    for num in nums:
        if num == 0:
            temp.append(0)
    for num in nums:
        if num == 1:
            temp.append(1)
    for num in nums:
        if num == 2:
            temp.append(2)
    for i in range(len(nums)):
        nums[i] = temp[i]

    return nums


def better_approach(nums):
    hashmap = {0: 0, 1: 0, 2: 0}
    for num in nums:
        hashmap[num] += 1

    i = 0
    for element, count in hashmap.items():
        while count != 0:
            nums[i] = element
            count -= 1
            i += 1

    return nums


def sort_approach(nums):
    nums.sort()
    return nums


def counts_approach(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    i = 0
    for _ in range(count_0):
        nums[i] = 0
        i += 1
    for _ in range(count_1):
        nums[i] = 1
        i += 1
    for _ in range(count_2):
        nums[i] = 2
        i += 1

    return nums


def dutch_national_flag_algorithm(nums):
    n = len(nums)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    return nums


print(brute_approach([1, 0, 2, 1, 0]))
print(brute_approach([0, 0, 1, 1, 1]))

print(better_approach([1, 0, 2, 1, 0]))
print(better_approach([0, 0, 1, 1, 1]))

print(sort_approach([1, 0, 2, 1, 0]))
print(sort_approach([0, 0, 1, 1, 1]))

print(counts_approach([1, 0, 2, 1, 0]))
print(counts_approach([0, 0, 1, 1, 1]))

print(dutch_national_flag_algorithm([1, 0, 2, 1, 0]))
print(dutch_national_flag_algorithm([0, 0, 1, 1, 1]))
