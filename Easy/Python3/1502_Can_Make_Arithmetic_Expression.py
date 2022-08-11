from typing import List

# A sequence of numbers is called an arithmetic progression if the difference 
# between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to 
# form an arithmetic progression. Otherwise, return false. 

# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with 
# differences 2 and -2 respectively, between each consecutive elements.

# Example 2:

# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic 
# progression.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0] # get the diff
        
        # use the look ahead approach
        for x in range(1, len(arr)):
            # find the difference and check if it's the same
            # as the one we calculated, return false if not
            if arr[x] - arr[x - 1] != diff:
                return False
        
        return True