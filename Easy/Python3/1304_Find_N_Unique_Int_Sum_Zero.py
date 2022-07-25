from typing import List

# Given an integer n, return any array containing n unique integers such that 
# they add up to 0.

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:

# Input: n = 3
# Output: [-1,0,1]

# Example 3:

# Input: n = 1
# Output: [0]

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        # divide n by 2, map each positive with it's negative num
        # to get n // 2 positive and n // 2 negative which sum
        # to zero. 
        #
        #
        #
        
        # special case if n is odd we include 0 because nothing maps to it
        if n % 2 == 1:
            return [x for x in range(n //2, n // 2 - n, -1)]
        # if n is even we don't include zero because it doesn't have a pair 
        else:
            return [x for x in range(n //2, n // 2 - n - 1, -1) if x != 0]