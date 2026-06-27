"""
- Given a string, reverse the string. The string input is given as array of characters.

Approach:
    - Using the two pointer swap procedure
    - TC -> O(n/2) -> O(n)
    - SC -> O(1)
        - As its done in place, with no extra space
"""

def reverse_string(str_arr):
    st = 0
    en = len(str_arr) - 1

    while st < en:
        tmp = str_arr[en]
        str_arr[en] = str_arr[st]
        str_arr[st] = tmp

        st += 1
        en -= 1
    print(str_arr)

reverse_string(['h','e','l','l','o'])