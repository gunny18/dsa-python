"""
- Given a string, reverse it. Using recursion
- Input is given as array of characters

Approach:
    - Remember in loop we used concept of swap and two pointers
    - Swap was the repeated step
    - For various values of start and end pointer
    - We do this as long as start < end
"""

def reverse_string(s, start, end):
    if start >= end:
        return
    s[start], s[end] = s[end], s[start]
    reverse_string(s, start+1, end-1)

s = ['h','e','l','l','o']

reverse_string(s,0,len(s)-1)
print(s)