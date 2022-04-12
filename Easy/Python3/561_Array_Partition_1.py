from typing import List
import heapq

# Given an array of 2n integers, your task is to group these integers into n 
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of 
# min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Convert the list into a heap then pop off 2 elements at a time to get
        # the two smallest values to add to the sum, this gives us the max value

        heapq.heapify(nums)
        total = 0
        
        while nums:
            total += min(heapq.heappop(nums), heapq.heappop(nums))
        
        return total
             
        """
        nums.sort()
        count = 0
        for x in range(0,len(nums),2):
            count+=nums[x]
        
        return count
        """

        """
        one liner version
        return sum(sorted(nums)[::2])
        """
