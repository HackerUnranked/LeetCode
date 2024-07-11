# You are given an integer array nums. In one operation, you can add or subtract
# 1 from any element of nums. Return the minimum number of operations to make 
# all elements of nums divisible by 3. 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 3

# Explanation:

# All array elements can be made divisible by 3 using 3 operations:

#     Subtract 1 from 1.
#     Add 1 to 2.
#     Subtract 1 from 4.

# Example 2:

# Input: nums = [3,6,9]

# Output: 0 

# Constraints:

#     1 <= nums.length <= 50
#     1 <= nums[i] <= 50
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # For a number x the biggest remainder is x - 1. for example if x = 4
        # then the reminder is 1. For the number 3 the posbile remainders are 0
        # 1 and 2. Since we can only add or subtract 1 from the number it means
        # if the reminder is 2 we can add to one to make it divisible by 3. If
        # the reminder is 1 we can subtract 1 to make it divisible by 3. We only
        # need these three operations to make any number divisible by 3.
        total = 0
        # loop through the numbers and check if the number is divisible by 3 and
        # if not add one to the total because we need to change it
        for x in nums:
            if x % 3 != 0:
                total += 1
        
        return total