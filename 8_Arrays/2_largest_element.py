"""
- Given array nums, return the largest element in the arrays.

Approach 1:
    - It is an unsorted array.
    - So I just keep comparing element by element and finally return largest
    - TC -> Worst case -> O(n)
        - My last element is the largest.

Approach 2:
    - What if I use 2 pointer method, so at a single iteration I can compare 2 elements.
    - This reduces number of iterations to half
    - TC -> O(n/2) ~~ O(n)
        - But we know this practically is more time efficient

Approach 3:
    - I can also using some sorting method and sort the array first
    - Then my last element is the maximum value
    - But. TC -> O(nlogn). SC -> O(1) + Stack space
        - Merge and Quick sort takes this.
        - Considering this, the array scanning solution proves better to find largest/smallest value

"""

def find_largest_1(nums):
    largest = nums[0]
    n = len(nums)
    if n == 1:
        return largest
    for i in range(1, n):
        if nums[i] > largest:
            largest = nums[i]
    
    return largest

def find_largest_2(nums):
    largest = nums[0]
    n = len(nums)
    if n == 1:
        return largest
    
    i = 1
    j = n-1
    while i <= j:
        if nums[i] > largest:
            largest = nums[i]
        if nums[j] > largest:
            largest = nums[j]
        i += 1
        j -= 1
    
    return largest

print(find_largest_1([3,3,0,99,-40]))
print(find_largest_2([3,3,0,99,-40]))