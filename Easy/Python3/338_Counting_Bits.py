from typing import List

# Given an integer n, return an array ans of length n + 1 such that for each i 
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0] # add zero first because there are no 1's
        
        # loop the numbers starting from 1 - n + 1
        for x in range(1,n + 1): 
            
            position = 0 # bit position
            count = 0 # count 1's
            
            # loop the 32 bits
            while position != 32:
                count += x & 1 # count if it's a one
                x = x >> 1 # shift right 1 bit
                position += 1 # increment bit position
            
            a.append(count) # append the number
        
        return a