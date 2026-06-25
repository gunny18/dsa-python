"""
N=5
Outout:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

def pattern(n):
    num = 1
    for i in range(1,n+1):
        for _ in range(1, i+1):
            print(num, end="")
            num += 1
        
        print()
pattern(5)