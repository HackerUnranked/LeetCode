from typing import List

# You are given an integer array nums (0-indexed). In one operation, you can 
# choose an element of the array and increment it by 1.

# For example, if nums = [1,2,3], you can choose to increment nums[1] to make 
# nums = [1,3,3].

# Return the minimum number of operations needed to make nums strictly 
# increasing.

# An array nums is strictly increasing if:
# 1. nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. 
# 2. An array of length 1 is trivially strictly increasing. 

# Example 1:

# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].

# Example 2:

# Input: nums = [1,5,2,4,1]
# Output: 14

# Example 3:

# Input: nums = [8]
# Output: 0

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num = 0 # keeps track of the total incrememnts
        prev = nums[0] # prevoius value after incremement
        
        # loop the array
        for x in range(1,len(nums)):
            # if they are equal we only need to increment 1 to make
            # the current value greater than the previous
            if prev == nums[x]:
                num += 1
                nums[x] += 1
            # previous is bigger so we need to increment the difference plus 1
            elif prev > nums[x]:
                to_add = (prev - nums[x]) + 1 # get the difference, add 1 to be greater
                nums[x] += to_add # add the difference to be greater than prev
                num += to_add # update the change in num
            
            prev = nums[x] # keep track of previous
        
        return num
        