"""
N=5
Outout:
1        1
12      21  
123    321
1234  4321
1234554321
"""

def pattern(n):
    for i in range(1,n+1):
        # Print left left num
        for num in range(1,i+1):
            print(num, end="")
        
        # Print space
        for space in range(1, 2*n-2*i+1):
            print(" ",end="")

        # Print right num
        for num in range(i,0,-1):
            print(num, end="")
        
        print()
pattern(5)