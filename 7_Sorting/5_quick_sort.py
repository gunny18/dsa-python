"""
- In merge sort, the TC was optimized but it took additional SC for temp array
- In quick sort we eliminate that
- TC still is the same
- It is also recursive so the the auxiliary stack space still remains in SC same as in merge sort due to recursion

Algorithm:
- We dont actually split/parition array, we logically do it
- Find pivot
    - Partition array into [<=Pivot],Pivot,[>Pivot]
        - Selection of pivot
            - 1st element/last/mid/random
        - Put pivot into correct position
            - Pseudocode:
                pivot = arr[start]
                i = start
                j = end
                Move i to a position where arr[i] >= pivot
                    - Why >=
                        - Coz we want even element equal to pivot on left partition
                    - Ensure i does not go beyond array i.e. end - 1
                    - Why end-1 ?
                        - We are moving i fwd.
                        - If i is at end, i++ would fail
                Move j into a position where arr[j] < pivot
                    - Ensure j does not go beyond arr boundary
                        - Ensure j does not go beyond array i.e. start + 1
                Swap arr[i] and arr[j]
                Do it until i < j

                - When we reach a point where j > i
                    - j is at the partition index
                    - Swap arr[j] and arr[low] (pivot)
                    - Not pivot is at partition index
                    - Everything to left is <= pivot
                    - Everything to right is > pivot
                    - Return partition index
- Repeat for left parition
- Repeat for right partition
"""

def partition(arr, start, end):
    pivot = arr[start]
    i = start
    j = end

    while i < j:
        while arr[i] <= pivot and i <= end - 1:
            i += 1
        while arr[j] > pivot and j >= start + 1:
            j -= 1
        # What if j > i once reached here ?
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # j is the partition index
    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(arr, start, end):
    if start >= end:
        return
    partition_index = partition(arr, start, end)
    quick_sort(arr, start, partition_index-1)
    quick_sort(arr,partition_index+1, end)
    return arr

arr = [4,6,2,5,7,9,1,3]
print(quick_sort(arr, 0, len(arr)-1))