from typing import List

# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space 
# complexity and O(n) runtime complexity?

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(0, len(nums)):
            if x != nums[x]:
                return x
            elif (x+1 == len(nums)) and (nums[len(nums)-1] != len(nums)):
                return len(nums)
            
            