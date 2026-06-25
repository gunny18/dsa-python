"""
N=5
Outout:
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""

"""
- A problem which requires a lot of observation
- This intuition of distances from top, left, bottom and right is after hours of analysis and observation pattern
- For such patterns where its not straight forward to recognize and patterns of this style remember the distance 
"""
def pattern(n):
    for i in range(1, 2*n):
        for j in range(1, 2*n):
            # dist from top
            top = i
            bottom = 2*n - i
            left = j
            right = 2*n-j
            horizontal_min = min(left, right)
            vertical_min = min(top, bottom)
            value = n - min(vertical_min, horizontal_min) + 1
            print(value, end="")

        print()
pattern(4)