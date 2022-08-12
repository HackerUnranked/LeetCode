# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every 
# occurrence should be counted.

# A substring is a contiguous sequence of characters in a string. 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".

# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", 
# "bca", "cab", and "abc".
#
# The good substrings are "abc", "bca", "cab", and "abc".

class Solution:
    def countGoodSubstrings_set(self, s: str) -> int:
        
        count = 0
        x = 0
        
        while x + 3 <= len(s): 
            # there are there unique characters
            if len(set(s[x:x+3])) == 3:
                count += 1    
            x += 1
        
        return count
    
    def countGoodSubstrings(self, s: str) -> int:
        
        count = 0
        x = 0
        
        while x + 3 <= len(s): 
            # compare each character of the substring
            if s[x] != s[x + 1] and s[x] != s[x + 2] and s[x + 1] != s[x + 2]:
                count += 1        
            x += 1
        
        return count