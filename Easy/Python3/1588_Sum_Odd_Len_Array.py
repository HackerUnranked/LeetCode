from typing import List

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# Example 2:

# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

# Example 3:

# Input: arr = [10,11,12]
# Output: 66

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        num = 0 # store the sum
        # this for loop gives us the odd lengths that we will partition
        for length in range(1, len(arr), 2):
            idx = 0 # starting point of the odd lengths to partition the sum
            while idx + length <= len(arr): # loop while we can still partition the array
                num += sum(arr[idx:idx+length]) # sum the odd partition
                idx += 1 # move the starting idx over one
        
        # this case if we are odd length then we will skip over the entire array sum so we
        # add it at the end
        if len(arr) % 2 != 0:
            num += sum(arr)
            
        return num