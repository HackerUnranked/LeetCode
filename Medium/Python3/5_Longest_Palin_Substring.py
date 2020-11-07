# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        for x in range(len(s)):
            # odd string
            word = self.helper(s, x, x)
            if len(word) > len(result):
                result = word
            # even string
            word = self.helper(s, x, x+1)
            if len(word) > len(result):
                result = word
        return result
    
    # get the longest palindrome, left, right are the middle indexes   
    # from inner to outer
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1; right += 1
        return s[left+1:right]