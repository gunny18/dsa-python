"""
N=5
Outout:
A
BB
CCC
DDDD
EEEEE
"""

def pattern(n):
    char = ord('A')
    for i in range(1,n+1):
        for _ in range(1, i+1):
            print(chr(char + i - 1), end="")
        
        print()
pattern(5)