# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where 
# A and B are valid parentheses strings, and + represents string concatenation.

#   For example, "", "()", "(())()", and "(()(()))" are all valid parentheses 
#   strings.

# A valid parentheses string s is primitive if it is nonempty, and there does 
# not exist a way to split it into s = A + B, with A and B nonempty valid 
# parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: 
# s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in
# the primitive decomposition of s.

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition:
# "(()())" + "(())".
# After removing outer parentheses of each part, this is:
# "()()" + "()" = "()()()".

# Example 2:

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition: 
# "(()())" + "(())" + "(()(()))".
#
# After removing outer parentheses of each part, this is:
# "()()" + "()" + "()(())" = "()()()()(())".

# Example 3:

# Input: s = "()()"
# Output: ""
# 3 Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # NOTE: in using a stack it means that when the stack
        # is empty after a pop that is the outermost parans for
        # a paran "set"
        #
        # example 1: s = "(()())(())", a = []
        # 
        # iter 1: a  =[(]
        # iter 2: a = [(, (]
        # iter 3: a = [(] # we popped because saw ) which means we had a pair
        # iter 4: a = [(, (]
        # iter 5: a = [(] # popped because we saw ) which means we had a pair
        # iter 6: a = [] # popped, this is a outer parans, don't include it since the stack is empty
        # copy skipping the first idx and last idx where the stack is empty and proceed scanning the
        # rest of the string repeating the steps above
        
        start = 0 # keep track of the outer most opened paran
        stack = [] # stack to keep track when we finished popping a sub paran 
        w = "" # concat the string
        
        # loop the string
        for idx,a in enumerate(s):
            # if we see an open paran then push it
            if a == '(':
                stack.append(a)
            else:
                # pop everytime we find a matching pair
                stack.pop()
                
                # if the stack is empty it means this is a substring
                # and we copy from the start idx + 1 to skip the start
                # of the outer most paran up to ending idx
                if stack == []:
                    w += s[start+1:idx] # copy the inner string skipping the outer open paran and closing
                    start = idx + 1 # move over the start paran so we scan for a new paran string
        
        return w