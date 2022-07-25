from re import I


from typing import List

# Given an integer array nums, return the greatest common divisor of the 
# smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer 
# that evenly divides both numbers. 

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

# Example 2:

# Input: nums = [7,5,6,8,3]
# Output: 1
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.

# Example 3:

# Input: nums = [3,3]
# Output: 3
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 3.
# The greatest common divisor of 3 and 3 is 3.

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # get the min and max num
        min_num = min(nums)
        max_num = max(nums)
        
        num = min_num # divisor, we use the min because min // max is 0
        
        # loop and count down from the min val and check if it can
        # divide both the max and min 
        while num != 0:
            # if the number divides both the it is the greatest
            # common divisor, break and return
            if max_num % num == 0 and min_num % num == 0:
                break
            num -= 1
        
        return num