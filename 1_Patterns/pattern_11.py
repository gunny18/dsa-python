"""
N=5
Outout:
1
01
101
0101
10101
"""

def pattern(n):
    for i in range(1,n+1):
        bit = i % 2
        for _ in range(1,i+1):
            print(bit,end="")
            # To flip bit
            bit = 1 - bit
            # To flip bit, using XOR (Same bit -> 0, Diff bit -> 1)
            # bit = bit ^ 1
        print()
pattern(5)