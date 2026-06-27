"""
- Given a string, check for palindrome

Approach:
    - Reverse array
    - Compare
    - TC -> O(n)
    - SC -> O(n)
        - Additional space to store original string (n characters)

Approach: 2 pointer approach
    - Here start with start and end pointer
    - Compare characters at either end, as long as start < end
    - If any are not equal, it is not a palindrome
    - TC -> O(n/2) ~ O(n)
    - SC -> O(1)
        - No extra space
"""

def check_palindrome(s):
    st = 0
    en = len(s) - 1

    while st < en:
        if s[st] != s[en]:
            return False
        st += 1
        en -= 1
    
    return True

print(check_palindrome("hannah"))
print(check_palindrome("Hannah"))
print(check_palindrome("aabbaaa"))