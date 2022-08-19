# Hercy wants to save money for his first car. He puts money in the Leetcode 
# bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to 
# Sunday, he will put in $1 more than the day before. On every subsequent Monday
# , he will put in $1 more than the previous Monday.

# Given n, return the total amount of money he will have in the Leetcode bank at 
# the end of the nth day. 

# Example 1:

# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

# Example 2:

# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
# (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

# Example 3:

# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
# (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

class Solution:
    def totalMoney(self, n: int) -> int:
   
        # create an array where the biggest num is going to be
        # 6 plus the total number of weeks because after each
        # week the max increases by 1
        #
        # example, n = 14
        
        # week 1 = [1, 2, 3, 4, 5, 6, 7]
        # week 2 = [2, 3, 4, 5, 6, 7, 8]
        # week 3 = [3, 4, 5, 6, 7, 8, 9]
        
        a = [y for y in range(1, 6 + (n // 7) + 1)]
        
        idx = n // 7 # get how many weeks we have
        total = 0 # incrememnt the total
        
        # if we don't have full weeks then we need
        # add an extra week to account for looping
        if n % 7 != 0:
            idx += 1
        
        # loop the index taking the sum from idx x to x + 7
        # where x is our monday since each monday we start at
        # a dollar more than the previous
        for x in range(idx):
            # if we have more than 7 days we keep taking the sum
            # of a week from idx x to x + 7
            if n >= 7:
                total += sum(a[x:x + 7])
                n -= 7 # subtrach the number of days we calculated
            # we have less than 7 days so just take the sum of the
            # remaining days from n
            else:
                total += sum(a[x:x + n])
                n = 0 # set n to zero so we can leave the loop
                
            if n == 0:
                return total # return the total