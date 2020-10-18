from typing import List

# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once. Find
# this single element that appears only once.

# Follow up: Your solution should run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # TODO: make this O(log n)
        uniques = {}
        for x in nums:
            if x not in uniques:
                uniques[x] = 1
            else:
                uniques[x] += 1
        
        for key in uniques:
            if uniques[key] == 1:
                return key