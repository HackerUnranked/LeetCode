# A parentheses string is valid if and only if:

#     It is the empty string,
#     It can be written as AB (A concatenated with B), where A and B are valid 
#     strings, or It can be written as (A), where A is a valid string.

# You are given a parentheses string s. In one move, you can insert a 
# parenthesis at any position of the string.

#     For example, if s = "()))", you can insert an opening parenthesis to be 
#     "(()))" or a closing parenthesis to be "())))".

# Return the minimum number of moves required to make s valid.

# Example 1:

# Input: s = "())"
# Output: 1

# Example 2:

# Input: s = "((("
# Output: 3

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_open = 0 # keeps track of the number of open parens
        counts = 0 # keeps track of how many parens we need to add to make this valid
        
        for par in s:
            if par == '(':
                num_open += 1 # add an openning paren
            else: # we are a closing, subtract from total if we have an open
                  # add to total sum if we are missing an openning
                if num_open == 0:
                    counts += 1
                else:
                    num_open -= 1 # subtract from the array the matching pair
        
        return counts + num_open
                