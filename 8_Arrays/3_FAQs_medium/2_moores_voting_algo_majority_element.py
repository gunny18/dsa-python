"""
- A very special counting mechanism to find majority element

Intuition
    - Consider the array [7,0,0,1,7,7,2,7,7]
    - Maintain 2 variables -> element & count
    - Start array traversal from 1st element -> 7
    - Now since this is the first element and count is till 0, we have only now started to traverse array
        - element -> Not started, count -> 0
        - nums[0] = 7 -> element -> 7, count -> 1, move next [Array traversal started]
        - nums[1] = 0 -> element -> 7, count -> 0, [Since array element is not 7, decrement count]
            - Since count has reached 0, upto this point all element occrrences cancel each other
            - None of them are majority
            - Just consider [7,0]
                - 7 appears once -> +
                - Then 0 appears -> -
                - They cancel, nobody dominates
        - nums[2] = 0 -> element -> 0, count -> 1 [Now start tracking count for element 0]
        - nums[3] = 1 -> element -> 0, count -> 0 [Reset element, since none dominates!]
        - nums[4] = 7 -> element -> 7, count -> 1 [Track counts of 7]
        - nums[5] = 7 -> element -> 7, count -> 2
        - nums[6] = 2 -> element -> 7, count -> 1
        - nums[7] = 7 -> element -> 7, count -> 2
        - nums[8] = 7 -> element -> 7, count -> 3
        Array done.
        We finally have element=7, count=3

    Interpreting result:
        - This says that there exists 7, 3 times, which is not dominated or cancelled at any other place by other elements
        - This says that if there exists an majority element it has to be element 7.
        - Else there is no majority element!!!

    Verify Majority:
        - Iterate array, count occurences of 7
        - Check if count > n/2.

    TC -> O(n) + O(n) ~~~ O(n)
    SC -> O(1)
        - Since it optimizes for space, it makes is a optimal solution, and the TC is only slightly increased,

    Since majority is guaranteed:
        - For this problem we can also skip the verification
"""


def majority_element_moores_voting_algo(nums):
    n = len(nums)
    ele = None
    count = 0

    for num in nums:
        if ele is None or count == 0:
            ele = num
            count += 1
        else:
            if num == ele:
                count += 1
            else:
                count -= 1

    if ele is not None and count:
        occ = 0
        for num in nums:
            if num == ele:
                occ += 1
                if occ > n / 2:
                    return ele


print(majority_element_moores_voting_algo([7, 0, 0, 1, 7, 7, 2, 7, 7]))
print(majority_element_moores_voting_algo([1, 1, 1, 2, 1, 2]))
print(majority_element_moores_voting_algo([-1, -1, -1, -1]))
