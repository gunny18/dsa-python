"""
N=5
Outout:
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

def pattern(n):
    # Upper half
    for i in range(1,n+1):
        # Star
        for _ in range(1, i+1):
            print("*", end="")

        # Space
        for _ in range(1, 2*n-2*i+1):
            print(" ", end="")

        # Star
        for _ in range(1, i+1):
            print("*", end="")
            
        print()

    # lower half
    for i in range(n-1,0,-1):
        # Star
        for _ in range(1, i+1):
            print("*", end="")

        # Space
        for _ in range(1, 2*n-2*i+1):
            print(" ", end="")

        # Star
        for _ in range(1, i+1):
            print("*", end="")

        print()
pattern(5)