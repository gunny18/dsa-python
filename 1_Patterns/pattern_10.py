"""
N=5
Outout:
*
**
***
****
*****
****
***
**
*
"""

def pattern(n):
    # Upper half
    for i in range(1,n+1):
        # Print *
        for i in range(1,i+1):
            print("*", end="")
        
        print()
    # Lower half
    for i in range(n-1,0,-1):
        # Print *
        for i in range(1,i+1):
            print("*", end="")

        print()
    

pattern(5)