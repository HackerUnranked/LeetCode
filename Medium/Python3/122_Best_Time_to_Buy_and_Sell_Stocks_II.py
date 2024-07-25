# You are given an integer array prices where prices[i] is the price of a given
# stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at
# most one share of the stock at any time. However, you can buy it then
# immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1)
# and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3)
# and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

# Example 2:

# Input: prices = [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1)
# and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

# Example 3:

# Input: prices = [7,6,4,3,1] Output: 0 Explanation: There is no way to make a
# positive profit, so we never buy the stock to achieve the maximum profit of 0.

 

# Constraints:

#     1 <= prices.length <= 3 * 104 0 <= prices[i] <= 104

from typing import List

# NOTE: This problem is exactly the same as
# 121_Best_Time_to_Buy_and_Sell_Stock.py The only difference is that we can buy
# and sell on the same day so we wil always buy if there is a gain. That is the
# new condition we have to add to the problem

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = None # This is the base case for the beginning of the list
        maxNum = 0 # This is the maximum difference between the maximum number and the minimum number
        second_max = 0 # This keeps track of us buying whenever we have a gain
        
        for idx,num in enumerate(prices):
            if prev == None:
                prev = num
            
            # Check if the previous max gain is bigger than current difference
            maxNum = max(maxNum, num - prev)
            
            # Check if we have a gain, this handles the case we always buy if
            # there is again
            if idx != 0:
                # compare if the current value is bigger than the previous and
                # if so calculate the gain
                if prices[idx] > prices[idx - 1]:
                    second_max += prices[idx] - prices[idx - 1]
                    
            # Update the minimum number if we find a new minimum number
            if num < prev:
                prev = num
                
        # Return the max between if we buy everytime we can vs buying once
        return max(maxNum, second_max)