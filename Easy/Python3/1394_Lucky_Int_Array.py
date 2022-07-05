from typing import List

# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

# Example 1:

# Input: arr = [2,2,3,4]
# explanation: The only lucky number in the array is 2 because frequency[2] == 2.

# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # bucket to count occurence
        bucket = [0]*500
        
        # map each value to it's correspounding index
        for val in arr:
            # we subtract 1 from the val because idx starts at 0
            bucket[val - 1] += 1
        
        to_return = -1 # return -1 if there are no lucky numbers that's why we set it at 0
        
        # loop through the bucket
        for idx,val in enumerate(bucket):
            # if the idx matches the val then it is a lucky number
            # we loop until the end so the biggest lucky should be captured
            # and no comp is needed
            if idx == val - 1:
                to_return = val
        
        # return the lucky number
        return to_return