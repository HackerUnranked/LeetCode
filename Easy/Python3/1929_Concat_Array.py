from typing import List

# Given an integer array nums of length n, you want to create an array ans of 
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
#  Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

class Solution:

    # using pythons extend functionn
    # time complexity is O(k) where k is the size of the list to be appended,
    # space complexity is O(n)
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
    
    # iterative solution, same time and space complexity
    def getConcatenation_iterative(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums.append(nums[x])
        
        return nums
    
    def getConcatenation_iterative_2(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums.append(num)