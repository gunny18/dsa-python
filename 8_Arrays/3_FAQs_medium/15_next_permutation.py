"""
Brute force solution:
    1. Generate all permutations
        - Needs a recursive solution
        - Time consuming
        - For n elements we will have n! permutations
        - Space needed is nxn!
    2. Linear search to find given sequence
    3. Find next sequence
    4. If its the last, circle back to first sequence as the next permutation

Next Permutation Algorithm:
    Say -> nums = [2,1,5,4,3,0,0]
    1. Longest Prefix intuition
        - Dictionary problem - same
        - When sorted, we know the ones with longer prefixes appear in order one after another
        - Until it breaks
        - In terms of the problem
            - Go from last, to find the break point
            - 0 -> 0 -> 3 -> 5 -> 1
            - At ele = 1, we have the breakpoint.
            - Untill then, if you imagine as a curve, its is always increasing, at ele=1, there is a dip
            FIND THE BREAKPOINT INDEX
    2. What if there is no dip/breakpoint ?
        - It means we are already given the largest possible permutation and need to circle back.
        - Reverse of it, will give the first permutation!
    3. In above case we found breakpoint index = 1. element = nums[1]
        - Now to find next permutation, we need to find what element can go in place of this breakpoint element
        - Has to be a value > 1 but smallest distance from 1
        - Which is 3
        - Swap 1 and 3, so we get
        [2,3,5,4,1,0,0]
    4. Notice, this does not break the intuition of the dip.
    5. Now simply reverse the array from breakpoint + 1 to end of array
        - We get [2,3,0,0,1,4,5]
        This is the next permutation

    TC:
        - n -> Dip/breakpoint
            - n -> reverse if no breakpoint
        - n -> Find element of longest prefix to replace the dip/breakpoint
        - n reverse -> from breakpoint + 1 to end
        ==> O(2n) or O(3n)
    SC:
        O(1)
"""


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def next_permutation_algorithm(nums):
    # Find breakpoint
    breakpoint = -1
    n = len(nums)
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            breakpoint = i
            break

    # Check if no breakpoint
    if breakpoint == -1:
        reverse(nums, 0, n - 1)
        return nums

    # Find the longest next prefix possible
    for i in range(n - 1, breakpoint, -1):
        if nums[i] > nums[breakpoint]:
            nums[i], nums[breakpoint] = nums[breakpoint], nums[i]
            break

    reverse(nums, breakpoint + 1, n - 1)

    return nums


print(next_permutation_algorithm([2, 1, 5, 4, 3, 0, 0]))
print(next_permutation_algorithm([2, 1]))
