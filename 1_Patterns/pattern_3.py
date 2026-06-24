"""
N=5
Outout:
1
12
123
1234
12345
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()


pattern(4)