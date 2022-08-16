from typing import List

# You are given an array of n strings strs, all of the same length.

# The strings can be arranged such that there is one on each line, making a grid
# . For example, strs = ["abc", "bce", "cae"] can be arranged as:

# abc
# bce
# cae

# You want to delete the columns that are not sorted lexicographically. In the 
# above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are 
# sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

# Return the number of columns that you will delete.

# Example 1:

# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 
# column.

# Example 2:

# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.

# Example 3:

# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        # create a bucket so we can map each string char to it's index
        bucket = [[] for x in range(len(strs[0])) ]
        total = 0
        
        for string in strs:
            # place each string at it's idx in the bucket
            for idx, val in enumerate(string):
                bucket[idx].append(val)
        
        for word in bucket:
            good = True
            for letters in range(len(word) - 1):
                if word[letters] > word[letters + 1]:
                    good = False
                    break
            
            if good == False:
                total += 1
                
        return total