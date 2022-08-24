# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).
# In one operation, you can select two indices x and y where 0 <= x, y < n 
# and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). 
# The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal. 

# Example 1:

# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

# Example 2:

# Input: n = 6
# Output: 9
# Exaplanation: arr[1,3,5,7,9,11]
# Sum of the array is 36, we have 6 numbers so we need all numbers to be 6
#
# 1. arr:[1,3,5,7,9,11]
# 2. arr:[6,3,5,7,9,6] subtract 5 from 11 and add it to 1, this is 5 steps
# 3. arr:[6,6,5,7,6,6] subtract 3 from 9 and add it to 3, this is 3 steps
# 4. arr[6,6,6,6,6,6]  subtract 1 from 7 and add it to 5, this is 1 step
# 5 + 3 + 1 = 9 steps


# The solution is essentially you start from the front and from the back of the array
# you move the right and left index over until you reach the middle index and you know you are
# done making the array equal. In our case we move only the right index until we reached a value
# where we are bigger than the equal value then we stop. We know we reached the middle.
# See example 2 above for more information
class Solution:
    def minOperations(self, n: int) -> int:

        val = 0

        for x in range(n):
            # each value is, (index * 2) + 1 for an array size n
            val += x*2 + 1

        # get the average of the numbers so we know what our target to reach
        # for each number is
        val //= n

        r = 0 # this is our index
        steps = 0 # steps we have taken
        go = True # makes the loop go
        
        while go:
            # calculate if we are bigger than the value we need to be
            # if we are not then find out how far we are off, this is
            # the number of steps since every +1 is a step
            if (2 * r + 1) < val:
                steps += val - (2*r + 1) # calculates the step
                r += 1 # move the index over 1
            # if we reached a value were the index is bigger than the value it means we
            # did all the steps already
            else:
                go = False
        
        return steps
            
            