from typing import List

# Given an array of positive integers nums, return the maximum possible sum of 
# an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i 
# where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

# Example 2:

# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum 
#              of 150.

# Example 3:

# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

class Solution:
    def maxAscendingSum_list(self, nums: List[int]) -> int:
        total = 0 # keeps track of the total
        prev = 0 # keeps track of the previous number
        a = [] # holds the sum values
        
        for w, x in enumerate(nums):
            # if we are ascending add to the total
            if prev < x:
                total += x
            # we reached a number that was small
            else:
                a.append(total) # add total to array
                total = x # set total as the new number that is smaller
            
            # if we are at the end append the total
            if w == len(nums) - 1:
                a.append(total)
            
            prev = x
        
        return max(a) # return the max
    
    def maxAscendingSum(self, nums: List[int]) -> int:
        total1 = 0 # keeps track of the total
        total2 = 0 # keeps track of the other total
        prev = 0 # keeps track of the previous number
        k = 0 # tells us which total we are incrementing
        
        for w, x in enumerate(nums):
            # if we are ascending add to the total
            if prev < x:
                # incremement the correct total
                if k == 0:
                    total1 += x
                else:
                    total2 += x
            # we reached a number that was small
            else:
                # check which one to keep
                if total1 > total2:
                    k = 1
                    total2 = x
                else:
                    k = 0
                    total1 = x
            
            prev = x
        
        # return the greater
        if total1 > total2:
            return total1
        
        return total2 