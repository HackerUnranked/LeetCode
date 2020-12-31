# A decimal number is called deci-binary if each of its digits is either 0 or 1
# without any leading zeros. For example, 101 and 1100 are deci-binary, while
# 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the
# minimum number of positive deci-binary numbers needed so that they sum up to n.

# Example 1:

# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
# We subtract using a dec-binary from each place holder
# 32
# 11, 32 becomes 21
# 11, 21 becomes 10
# 10, 10 beccomes 00
# so 3 is number of deci-binary numbers and it also matches the highest number 
# in the string which is 3  


# Example 2:

# Input: n = "82734"
# Output: 8
# 82734
# 11111, 82734 becomes 71623
# 11111, 71623 becomes 60512
# 10111, 60512 becomes 50401
# 10101, 50401 becomes 40300
# 10100, 40300 becomes 30200
# 10100, 30200 becomes 20100
# 10100, 20100 becomes 10000
# 10000, 10000 becomes 00000
# so 8 is the number of deci-binary numbers which also matches the highest number
# in the string which is 8

# Example 3:
# Input: n = "27346209830709182346"
# Output: 9

class Solution:
    def minPartitions(self, n: str) -> int:
        # just find the biggest digit in the string and return it
        return max(n)