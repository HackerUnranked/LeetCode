# Given an integer n, return a string with n characters such that each character 
# in such string occurs an odd number of times.

# The returned string must contain only lowercase English letters. If there are 
# multiples valid strings, return any of them.  

# Example 1:

# Input: n = 4
# Output: "pppz"
# Explanation: "pppz" is a valid string since the character 'p' occurs three 
# times and the character 'z' occurs once. Note that there are many other valid 
# strings such as "ohhh" and "love".

# Example 2:

# Input: n = 2
# Output: "xy"
# Explanation: "xy" is a valid string since the characters 'x' and 'y' occur 
# once. Note that there are many other valid strings such as "ag" and "ur".

# Example 3:

# Input: n = 7
# Output: "holasss"

class Solution:
    def generateTheString(self, n: int) -> str:
        # if the string is even then we do n - 1 of the same
        # character to get it n odd then the remaining 1 character
        # will also be odd
        #
        # example n = 4
        # biggest odd num is 3
        # aaab where 3 is odd and b is odd
        #
        #
        # if the string is odd then return a character n times
        
        # the string is even
        # return n - 1 a to get an odd
        # return 1 b to get another odd
        if n % 2 == 0:
            return ('a'*(n-1))+'b'
        
        return 'a'*n # the string is odd return a character n times