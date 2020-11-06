from typing import List

# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in range(1,len(nums)):
            nums[0]^=nums[x]
        
        return nums[0]