from typing import List
# There are 3n piles of coins of varying size, you and your friends will take 
# piles of coins as follows:

#     In each step, you will choose any 3 piles of coins 
#     (not necessarily consecutive).
#     
#     Of your choice, Alice will pick the pile with the maximum number of coins.
#     You will pick the next pile with the maximum number of coins.
#     Your friend Bob will pick the last pile.
#     Repeat until there are no more piles of coins.

# Given an array of integers piles where piles[i] is the number of coins in the 
# ith pile.

# Return the maximum number of coins that you can have. 

# Example 1:

# Input: piles = [2,4,1,2,7,8]
# explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, 
# you the pile with 7 coins and Bob the last one.
# 
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile 
# with 2 coins and Bob the last one.
# 
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only 
# get 2 + 4 = 6 coins which is not optimal.

# Example 2:

# Input: piles = [2,4,5]
# Output: 4

# Example 3:

# Input: piles = [9,8,7,6,5,1,2,3,4]
# Output: 18

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        bucket = [0] * max(piles) # bucket so we can sort in ascending
        take = 0 # keeps track of who is taking
        total = 0 # keeps track of the total we took
        idx = 0 # idx to traverse the numbers
        num3 = 0 # we use this to take the smallest numbers first for bob that 
                 # we we are left with only the big numbers to chose from for us 
        
        # sort the numbers
        for x in piles:
            bucket[x - 1] += 1 # count the numbers
        
        # loop the sorted bucket
        while idx < len(bucket):
        
            if bucket[idx] != 0:
                # first get all the small numbers for bob
                if num3 != len(piles) // 3:
                    num3 += 1
                else: # we took all the small numbers so now we just
                      # take for us and alice by taking turns
                    take += 1 # take a number
                    
                    # if we are picking then add it to the total
                    if take == 1:
                        total += idx + 1
                    # reset because alice took
                    else:
                        take = 0
                    
                bucket[idx] -= 1 # subtract the one we took
            
            if bucket[idx] == 0:
                idx += 1 # increment the idx so we can move to the next number
        
        return total
    
    # using the sort function
    def maxCoins_Sort(self, piles: List[int]) -> int:
        piles.sort() # sort the list
        temp = piles[len(piles) // 3:len(piles)] # slice the array
        total = 0
        idx = 0
        
        # take turns taking coins between us and alice
        while idx < len(temp):
            total += temp[idx]
            idx += 2
        
        return total