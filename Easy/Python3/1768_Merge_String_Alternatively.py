# You are given two strings word1 and word2. Merge the strings by adding letters 
# in alternating order, starting with word1. If a string is longer than the 
# other, append the additional letters onto the end of the merged string.

# Return the merged string. 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w = "" # string to create
        idx = 0
        
        # loop each string and keep concating until we reached
        # the end of a string
        while idx < len(word1) and idx < len(word2):
            # create the string with the word1 char first then word2 second
            w += word1[idx] + word2[idx]
            idx += 1 # move the idx move
        
        # if word1 is bigger we append the rest of it's char at the end of
        # the string
        if len(word1) > len(word2):
            w += word1[idx:]
        # append the rest of word2 it is bigger
        else:
            w += word2[idx:]
        
        
        return w