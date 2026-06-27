"""
- Given a number string. Find the substring that has largest odd number sub string
- Input can have leading 0's
- Output must not have leading 0's

Approach 1:
    - For each number, you find combinations which produce odd numbers
    - Then you iterate over combinations to find the largest odd number
    - TC -> O(nxn) + O(num_odd_combinations)

Approach 2:
    - We can say if a number is odd from the last digit ?
    - Yes
    - So we iterate from last
        - Stop when digit is odd
        - Thats the last index of string we need
    - Now find start index
        - To handle leading 0's case
    
    - TC -> O(n) + O(last index for odd string) ~ O(n)
    - SC -> O(n), though we return sub string, its still going to be a new string, not inplace modification
"""

def largest_odd_substring(s):
    last_odd_idx = -1
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 1:
            last_odd_idx = i
            break
    
    # Find start idx
    j = 0
    while j <= last_odd_idx:
        if int(s[j]) == 0:
            j += 1
        else:
            break
    
    return s[j:last_odd_idx+1]

print(largest_odd_substring("5347"))
print(largest_odd_substring("0214638"))
print(largest_odd_substring("0032579"))
print(largest_odd_substring("003002579"))
