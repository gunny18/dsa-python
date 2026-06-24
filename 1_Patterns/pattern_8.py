"""
N=5
Outout:  
*********
 *******
  *****
   ***
    *
"""

def pattern(n):
    for i in range(n,0,-1):
        # Print left space
        for _ in range(1,n-i+1):
            print(" ",end="")
        
        # Print *
        for _ in range(1,2*i):
            print("*",end="")

        # Print right space
        for _ in range(1,n-i+1):
            print(" ",end="")
        
        print()


pattern(5)