from typing import List

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position 
# moves to indices[i] in the shuffled string.

# Example: 4 5 6 7 0 2 1 3
#          c o d e l e e t
# 
#          0 1 2 3 4 5 6 7 
#          l e e t c o d e 

# Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        bob ={}
        for x,y in enumerate(indices):
            bob[y] = s[x]
        
        new_str = ""
        for k,y in sorted(bob.items()):
            new_str+= bob[k]
        
        return new_str