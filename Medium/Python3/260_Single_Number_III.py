from typing import List

# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
# Follow up: Your algorithm should run in linear runtime complexity. Could you 
# implement it using only constant space complexity?

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        uniques = {}
        
        for x in nums:
            if x not in uniques:
                uniques[x] = 1
            else:
                uniques[x] += 1
        
        return [key for key,value in uniques.items() if uniques[key] == 1]