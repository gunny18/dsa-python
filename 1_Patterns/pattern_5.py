"""
N=5
Outout:
*****
****
***
**
*
"""

def pattern(n):
    for i in range(n,0,-1):
        for _ in range(1,i+1):
            print("*",end="")
        print()


pattern(5)