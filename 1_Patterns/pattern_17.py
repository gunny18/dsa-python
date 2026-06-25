"""
N=5
Outout:
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

def pattern(n):
    for i in range(1,n+1):
        # Left space
        for s in range(1, n-i+1):
            print(" ", end="")
        
        # Chars
        char = ord('A') - 1
        for j in range(1, 2*i):
            if j <= i:
                char = char + 1
            else:
                char = char - 1
            print(chr(char), end="")

        # Right space
        for s in range(1, n-i+1):
            print(" ", end="")
    
        print()
pattern(5)