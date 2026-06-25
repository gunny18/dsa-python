"""
N=5
Outout:
A
AB
ABC
ABCD
ABCDE
"""

def pattern(n):
    for i in range(1,n+1):
        char = ord('A')
        for _ in range(1, i+1):
            print(chr(char), end="")
            char += 1
        
        print()
pattern(5)