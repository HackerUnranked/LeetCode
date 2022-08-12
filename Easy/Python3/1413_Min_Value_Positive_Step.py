from typing import List

# Given an array of integers nums, you start with an initial positive value 
# startValue.

# In each iteration, you calculate the step by step sum of startValue plus 
# elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step 
# sum is never less than 1.

# Example 1:

# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by 
# step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

# Example 2:

# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive. 

# Example 3:

# Input: nums = [1,-2,-3]
# Output: 5

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prev_sum = 0 # keeps track of the sums
        
        # the biggest the number could be is 100 * 100
        # because the max array size is 100 and the max
        # max number is 100, we add 1 so we know everything
        # will be smaller for our base case
        small = (100 * 100) + 1
        
        # find where the sum is the lowest
        for x in nums:
            prev_sum += x
            # if the sum is smaller swap
            if prev_sum < small:
                small = prev_sum
        
        # if the smallest sum is greater than zero then return 1 because the smallest value we can be is 1
        if small > 0:
            return 1
        # get the absolute value and minus 1 to get the number above 1
        else:
            return abs(small - 1)