from typing import List

# Given a 0-indexed integer array nums of length n and an integer k, return the 
# number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and 
# (i * j) is divisible by k. 

# Example 1:

# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4 
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

# Example 2:

# Input: nums = [1,2,3,4], k = 1
# Output: 0
# Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0 # count the pairs
        for idx in range(len(nums)): # loop the idx
            # loop the idx again but only look at the ones we haven't seen from
            #  the curret idx
            for idx2 in range(idx+1, len(nums)):
                # if the idx val are the same and the division works the we 
                # count
                if nums[idx] == nums[idx2] and idx * idx2 % k == 0: 
                    count += 1              
        return count