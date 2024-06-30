# Given a sorted array of distinct integers and a target value, return the index 
# if the target is found. If not, return the index where it would be if it were
# inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        for x,y in enumerate(nums):
            # if we found the target or the current
            # number is greater than the target then
            # return x because that is where the target
            # should be placed
            if y == target or y > target:
                return x
        
        return len(nums)
    
    # This is the binary search solution
    def binarySearchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # Get the start and end index
        
        # Loop up until the end of the array
        while left <= right:
            # Get the middle index of the array, this floors mid so we always get the lowest value
            mid = (left + right) // 2
            
            # Check if the middle is the target and if so then return the index
            if nums[mid] == target:
                return mid
            # If the mid is smaller than the target then we shift the left index
            # to start at the second half of the array. We do a  + 1 so we can
            elif nums[mid] < target:
                left = mid + 1
            # If mid is greather than the target then we shift the right index to discard the larger half
            else:
                right = mid - 1
        
        return left
                