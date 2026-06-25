"""
N=5
Outout:
ABCDE
ABCD
ABC
AB
A
"""

def pattern(n):
    for i in range(n,0,-1):
        char = ord('A')
        for _ in range(1, i+1):
            print(chr(char), end="")
            char += 1
        
        print()
pattern(5)