# Given two integers, num and t. A number is achievable if it can become equal to 
# num after applying the following operation:

#    Increase or decrease the number by 1, and simultaneously increase or 
#    decrease num by 1.

# Return the maximum achievable number after applying the operation at most t 
# times.

# Example 1:

# Input: num = 4, t = 1

# Output: 6

# Explanation:

# Apply the following operation once to make the maximum achievable number equal to num:

#     Decrease the maximum achievable number by 1, and increase num by 1.

# Example 2:

# Input: num = 3, t = 2

# Output: 7

# Explanation:

# Apply the following operation twice to make the maximum achievable number 
# equal to num:

#     Decrease the maximum achievable number by 1, and increase num by 1.

# This problem is telling us we are given a number num and can either increase
# or decrease it by 1 only t times. We need to find the biggest number we can
# get after t operations. Afterwards we need to see what is the new biggest number
# we can get after t operations is.
#
# Approach:
#
# 1. Increase num t times.
# 2. return num + t to get the new biggest number we can get after t operations.

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t + t