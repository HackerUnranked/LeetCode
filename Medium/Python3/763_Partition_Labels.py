from typing import List

# You are given a string s. We want to partition the string into as many parts 
# as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in 
# order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits s into less parts.

# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == None:
            return []
        
        arr = [] # the output of our answer
        last = [-1] * 26 # keeps track of the last occurence of a letter at the indx
        
        # fill up an array of the last idx we seen each letter at
        for idx, letter in enumerate(s):
            last[ord(letter) - 122] = idx # set the idx we seen the letter at in the array
        
        # keeps track of our substring
        start = 0
        end = 0
        
        for idx1, letter1 in enumerate(s):
            # get the idx the current character last appeared at, we keep updating this
            # and only keep where the end of the substring is greatest because we want
            # to account for all characters
            end = max(end, last[ord(letter1) - 122])
            
            # this means we found a partition that is valid because we reached
            # the end of the substring
            if idx1 == end:
                arr.append(end - start + 1) # calculate the string size
                start = end + 1 # adjust the starting boundary to move onto a new partition
        
        return arr
                