from typing import List

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

# Example 1:

# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and 
# "attend".

# Example 2:

# Input: words = ["leetcode","win","loops","success"], pref = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        the_sum = 0
        
        # loop the words
        for word in words:
            # if the word is greater then it could be a prefix
            if len(word) >= len(pref):
                # string slice to check if the beginning of the word matches the pref
                if word[0:len(pref)] == pref:
                    the_sum += 1 # increment count
        
        return the_sum