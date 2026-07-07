"""
Given an integer array nums, return a list of all the leaders in the array.

A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.

Approach 1: Brute force
    - 1 element at a time

    TC ~~ O(nxn)
    SC -> O(n)

Approach 2: Start from right and use definition of leader element
    - So always maintain 2 variables -> prev_leader, prev_element
    - Last is always a leader -> gets initialised as prev ele and leader
    - Compare if ele is > than prev leader and prev ele
        - Update prev ele and leader respectively
        - At each point if leader is found, put in new array
    - Go until start of array

    - Now the result array has to be reversed to get final leader array, in order

    TC -> O(n) + O(n)
    SC -> O(n)

Approach 3: Same as approach 2
    - Some tweaks here are in the logic
    - So only keep track of the leader.
    - That leader is the maximum at any point of all the elements on right of curr element
    - So I need to compare only with it
"""


def leaders_in_array_app2(nums):
    n = len(nums)
    if n == 1:
        return nums
    prev_element, prev_leader = nums[-1], nums[-1]
    leaders = [prev_element]
    for i in range(n - 2, -1, -1):
        if nums[i] > prev_element and nums[i] > prev_leader:
            leaders.append(nums[i])
            prev_leader = nums[i]
        prev_element = nums[i]

    leaders.reverse()
    return leaders


def leaders_in_array_app3(nums):
    n = len(nums)
    max_from_right = None
    leaders = []
    for i in range(n - 1, -1, -1):
        if max_from_right is None or nums[i] > max_from_right:
            leaders.append(nums[i])
            max_from_right = nums[i]
    leaders.reverse()
    return leaders


print(leaders_in_array_app2([1, 2, 5, 3, 1, 2]))
print(leaders_in_array_app2([-3, 4, 5, 1, -4, -5]))

print(leaders_in_array_app3([1, 2, 5, 3, 1, 2]))
print(leaders_in_array_app3([-3, 4, 5, 1, -4, -5]))
