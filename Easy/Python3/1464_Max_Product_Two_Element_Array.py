from typing import List

# Given the array of integers nums, you will choose two different indices i and 
# j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will 
# get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

# Example 2:

# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get 
# the maximum value of (5-1)*(5-1) = 16.

# Example 3:

# Input: nums = [3,7]
# Output: 12

class Solution:
    # sort using pythons method and return the product of the last two ints
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)
    
    # O(n) solution without using python sort method
    def maxProduct_linear(self, nums: List[int]) -> int:
        first, second = 0, 0
        
        # loop the numbers and find the to biggest
        for num in nums:
            # if the first is smaller or equal then we swap
            if first <= num:
                second = first # update biggest to second biggest
                first = num # update new biggest val
            elif second < num: # this handles the case where first is the biggest already therefore we just need to update second
                second = num
                
        return (first - 1) * (second - 1)