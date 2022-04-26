from typing import List

# Given an array of integers A sorted in non-decreasing order, return an array 
# of the squares of each number, also in sorted non-decreasing order.

# Example 1:

# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])

# O(n) time complexity and O(n) space. This is using the two pointers approach
class Solution_1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        my_array = [0]*len(nums) # create an array of size nums
        idx = len(nums) - 1 # the idx so we can insert biggest at the end
        beg = 0 # left half
        end = len(nums) - 1 # right half
        
        while idx >= 0:
            # the end is bigger insert it
            if abs(nums[beg]**2) < abs(nums[end]**2):
                my_array[idx] = nums[end]**2
                end -= 1
            # insert the right half itis bigger OR they are equal
            else:
                my_array[idx] = nums[beg]**2
                beg += 1
            idx -= 1
        
        return my_array