from typing import List

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        to_add = []
        
        if nums == None:
            return
        elif len(nums) == 0:
            return
        
        for x in nums:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        
        for y in even:
            to_add.append(y)
            to_add.append(odd.pop())
        
        return to_add
        
                