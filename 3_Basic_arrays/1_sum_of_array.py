"""
- Given array of size n, find sum of all elements in array.

Algorithm:
    - Traverse each element, index wise
    - Increment sum
    - TC -> O(n)
    - SC -> O(1)
"""

def sum_array(arr, n):
    sum = 0
    for i in range(0,n):
        sum += arr[i]
    return sum

print(sum_array([1,2,3,4],4))
print(sum_array([1,2,3,4,-1,10],6))