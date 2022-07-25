from typing import List

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number 
# of occurrences (i.e., the same frequency). 

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All 
# characters occur 2 times in s.

# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of 
# times.

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        buckets = [0]*26
        
        for x in s:
            buckets[ord(x) - 97] += 1
        
        seen = 0
        
        for x in buckets:
            # capture the number that isn't a zero
            # and compare with all the other numbers
            # that aren't zero, we should return false
            # if we see another number that isn't the
            # same otherwise return true
            if x != 0 and seen == 0:
                seen = x
            elif x != seen and x != 0:
                return False
        
        return True