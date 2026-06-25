"""
N=5
Outout:
E
DE
CDE
BCDE
ABCDE
"""

def pattern(n):
    char = ord('A') + n - 1
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(chr(char + j - 1), end="")

        char -= 1
        print()
pattern(5)