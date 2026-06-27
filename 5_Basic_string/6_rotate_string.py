"""
- Given a string, and a goal, check if the string can be converted into a goal with a number of shitfs
- 1 shift it moving leftmost character to the righmost position


Approach 1:
    - We just compare goal and shifted string
    Analysis:
        Ex -> s="abcde" goal="cdeab"
        - 0 Shifts -> Compare s and goal
        - 1 shift -> bcdea compare to goal
        - 2 shift -> cdeab compare to goal
        - 3 shift -> deabc compare to goal
        - 4 shift -> eabcd compare to goal
        - 5 shift -> abcde compare to goal
            - 5th shift gives original string
            - So at max we need to do 0 to n-1 shifts
    - TC
        - Outer loop of n times
            - In each loop we need to find substring -> left and right
            - For 1 shift left = s[0], right = s[1:]
            - So n-1,n-2,... -> roughly n unit of time
        - ~ O(nxn)
    - SC -> O(n)

Approach 2 - Double string method
    - We take the string s, concatenate with s itself
    - Now we just compare substring of double s upto length of org s with goal
    - Here only advantage is we dont have to build left and right substring.
    - We can just keep comparing goal with double s
    Ex -> s="abcde" goal="cdeab"
        - double s = abcdeabcde
        Again shifts from 0 to n-1
            - goal substr of double s[0:]
            - goal substr of s[1:]
            - goal substr of s[2:]
            - goal substr of s[3:]
            - goal substr of s[4:]
        Now stop
        - Difference here is we are not coputing subring
        - We are only checking if goal (substr) exists in double s
        - String finds are already optimised internally hence this is opimised even more
"""

def brute_force_approach(s, goal):
    if s == goal:
        return True
    for shifts in range(1, len(s)):
        left = s[:shifts]
        right = s[shifts:]
        if goal == right + left:
            return True
    return False

def double_string_method(s:str, goal):
    double_s = s + s
    for shift in range(0, len(s)-1):
        # We can even just do goal in double_s[shift:]
        if goal == double_s[shift:shift+len(s)]:
            return True
    return False

print(brute_force_approach('abcde','adeac'))
print(brute_force_approach('abcde','cdeab'))

print(double_string_method('abcde','adeac'))
print(double_string_method('abcde','cdeab'))
