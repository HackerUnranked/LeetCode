# A string is a valid parentheses string (denoted VPS) if it meets one of the following:

# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# Given a VPS represented as string s, return the nesting depth of s.

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.
# Example 2:

# Input: s = "(1)+((2))+(((3)))"
# Output: 3
# Example 3:

# Input: s = "1+(2*3)/(2-1)"
# Output: 1
# Example 4:

# Input: s = "1"
# Output: 0

class Solution:
    def maxDepth(self, s: str) -> int:
        max_num = 0
        cur_max = 0
        
        for x in s:
            
            if x == '(':
                cur_max += 1
                if cur_max > max_num:
                    max_num = cur_max
            elif x == ')':
                cur_max -= 1
        
        return max_num