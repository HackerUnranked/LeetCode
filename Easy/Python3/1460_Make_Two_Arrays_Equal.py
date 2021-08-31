from typing import List

# Given two integer arrays of equal length target and arr.

# In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

# Return True if you can make arr equal to target, or False otherwise.

# Example 1:

# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
# 3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.

# Example 2:

# Input: target = [7], arr = [7]
# Output: true
# Explanation: arr is equal to target without any reverses.

# Example 3:

# Input: target = [1,12], arr = [12,1]
# Output: true

# Example 4:

# Input: target = [3,7,9], arr = [3,7,11]
# Output: false
# Explanation: arr doesn't have value 9 and it can never be converted to target.

# Example 5:

# Input: target = [1,1,1,1,1], arr = [1,1,1,1,1]
# Output: true

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Basically we are being asked if the two arrays are the same
        # they are unsorted
        
        # base case if the lists are empty or if they don't match in size
        if target == None or arr == None:
            return False
        elif len(target) == 0 or len(arr) == 0:
            return False
        
        # create a dictionary to store the count of each character than appeared
        count_target = {}
        
        for x in target:
            if x not in count_target:
                count_target[x] = 1
            else:
                count_target[x] += 1
        
        # loop through the second array and subtract it if we seen it, if it is new then we exit
        for y in arr:
            if y in arr:
                if y not in count_target:
                    return False
                else:
                    if count_target[y] - 1 < 0:
                        return False
                    else:
                        count_target[y]  -= 1
        
        return True