# You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example 1:

# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# Example 2:

# Input: order = "cbafg", s = "abcd"
# Output: "cbad"

# S is the string of characters and order is the order the characters must be in 
# S = "fabaccbas"
# order = "abc"
# answer = aaabbccfs

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        l = []
        
        # count how many of each character appears in the string
        for x in order:
            # if the charater in order is in S then append it to the list and count how many occurrence
            l.append(x*s.count(x))
        # if the string contains a character that isn't in order, append it to the end
        for x in s:
            if x not in order:
                l.append(x)
        # join the list to create a string
        return ''.join(l)
        