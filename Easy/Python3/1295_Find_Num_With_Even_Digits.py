from typing import List

# Given an array nums of integers, return how many of them contain an even 
# number of digits.
 
# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a = 0 # count for how many number is of even length
        
        # loop each num in the list
        for num in nums:
            
            count = 1 # count for how many digit is in a number, note a number has at least 1 digit
            
            # loop if the number is greater or equal to 10 because it means it contains at least
            # 2 digits therefore possibly even
            while num >= 10:
                
                num = num // 10
                count += 1 # each time we divide by 10 we count 1 digit from the number
            
            # increment the even length digit count if we seen an
            # even count of digit from the number
            if count % 2 == 0:
                a += 1
        
        return a
                    
                    