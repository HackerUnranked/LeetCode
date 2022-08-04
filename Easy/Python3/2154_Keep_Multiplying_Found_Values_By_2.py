from typing import List

# You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

# You then do the following steps:

#     If original is found in nums, multiply it by two (i.e., set original = 2 * original).
#     Otherwise, stop the process.
#     Repeat this process with the new number as long as you keep finding the 
# number.

# Return the final value of original. 

# Example 1:

# Input: nums = [5,3,6,1,12], original = 3
# Output: 24
# Explanation: 
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.

# Example 2:

# Input: nums = [2,7,9], original = 4
# Output: 4
# Explanation:
# - 4 is not found in nums. Thus, 4 is returned.

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        nums.sort() # sort the list from least to greatest
        
        for x in nums:
            # if we reached a number bigger than us it means
            # we couldn't find original, return
            if x > original:
                return original
            # if we found the number, double original and keep searching
            elif x == original:
                original *= 2
        
        return original # return original, we either found the number or didn't
    
    # using boolean to set flags
    def findFinalValue_bool(self, nums: List[int], original: int) -> int:
        arr = [False] * 1000 # multiply by 1000 because the number constraint is 1000
        
        # mark if we seen the number
        for a in nums:
            arr[a - 1] = True
        
        for things in range(len(nums)):
            # we check if we seen the number, we do the 1000 check because
            # of the contraint the number should never exceed 1000
            if original > 1000 or arr[original - 1] == False:
                return original
            
            original *= 2 # double because we seen it
        
        return original  