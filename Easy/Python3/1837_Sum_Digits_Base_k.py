# Given an integer n (in base 10) and a base k, return the sum of the digits of 
# n after converting n from base 10 to base k.

# After converting, each digit should be interpreted as a base 10 number, and 
# the sum should be returned in base 10.

# Example 1:

# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

# Example 2:

# Input: n = 10, k = 10
# Output: 1
# Explanation: n is already in base 10. 1 + 0 = 1.

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # to convert a number to base x
        # we mod the number by k and
        # get the remainder then divide
        # the number by k and repeat
        # until we reach zero
        
        sm = 0
        while n > 0:
            sm += n % k # add the remainder after mod
            n //= k # # add how many times divisible
        return sm # return val
    
    # example, n = 34, k = 5
    #
    # sm = 34 % 5 = 4 remainder
    #
    # n // 6 = 5
    #
    #
    # sm = 4 + (5 % 6) = 4 + 6 = 9
    #
    # n = 5 // 6 = 0
    #
    # sm = 9 and return