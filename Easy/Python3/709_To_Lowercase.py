# Given a string s, return the string after replacing every uppercase letter 
# with the same lowercase letter.

# Example 1:

# Input: s = "Hello"
Output: "hello"

# Example 2:

# Input: s = "here"
# Output: "here"

# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, s: str) -> str:
        w = "" # our final results
        for a in s:
            # if the string is uppercase then we will change it to lower case
            if a.isupper() == True:
                a = a.lower()
            # concat the string
            w += a
        
        return w
    
    # one liner using pyton library
    def toLowerCase_OneLiner(self, s: str) -> str:
        return s.lower()