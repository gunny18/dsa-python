"""
- Given a string check if string is palindrome, using recursion

Approach:
- Here also we implement the 2 pointer aproach using head recursion.
- Breaking down to compare exactly 2 opposite chars at each step and aggregating the results
"""

def check_palindrome(s, start, end):
    if start >= end:
        return True
    
    return (s[start] == s[end]) and check_palindrome(s, start+1, end-1)

# s = "hannah"
s = "aabbaA"

print(check_palindrome(s, 0, len(s)-1))