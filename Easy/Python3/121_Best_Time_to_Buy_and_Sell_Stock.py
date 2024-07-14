# You are given an array prices where prices[i] is the price of a given stock on
# the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot
# achieve any profit, return 0.
#
# 
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1)
# and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and
# selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
#
# Input: prices = [7,6,4,3,1] Output: 0 Explanation: In this case, no
# transactions are done and the max profit = 0.
#
# 
#
# Constraints:
#
#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea is to keep track of the minimum number and the maximum number. Everytimne we find a new minimum number, we update the minimum number and reset the maximum number. If we find a new maximum number, we update the maximum number. We keep track of the maximum difference between the maximum number and the minimum number.
        prev = None # This is the base case for the beginning of the list
        maxNum = 0 # This is the maximum difference between the maximum number and the minimum number
        
        for num in prices:
            if prev == None:
                prev = num
            
            # Get the maximum difference between the maximum number and the minimum number
            maxNum = max(maxNum, num - prev)

            # Update the minimum number if we find a new minimum number
            if num < prev:
                prev = num
        # Return the maximum difference between the maximum number and the minimum number
        return maxNum