from typing import List

# Given a string S that only contains "I" (increase) or "D" (decrease),
# let N = S.length.

# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]

#Example 1:

# Input: "IDID"
# Output: [0,4,1,3,2]

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        I = 0
        D = len(S)
        to_return = []
        
        for x in S:
            if x == 'I':
                to_return.append(I)
                I+= 1
            else:
                to_return.append(D)
                D -= 1
                
        to_return.append(D)
        
        return to_return