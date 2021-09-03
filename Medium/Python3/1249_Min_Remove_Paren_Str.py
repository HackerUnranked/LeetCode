# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', 
# in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Example 4:

# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stacks = []
        new_str = []
        
        for x in s:
            # if i am a letter then i add myself to the list
            if x != ')' and x != '(':
                new_str.append(x)
            # if i am a open parens then i add myself
            elif x == '(':
                # add myself to the stack and array
                stacks.append(x)
                new_str.append(x)
            # if i am closing, see if i can pop, if i can't then don't add
            elif x == ')':
                if len(stacks) != 0:
                    stacks.pop()
                    new_str.append(x)
        
        # if the string is empty it means it just contains parens
        if len(new_str) == 0:
            return ""
        else:
            # we need to reverse the string because remove() removes the first occurence, we want the last
            new_str.reverse()
            
            # remove the unpaired open parens from the string and pop off from the stack
            while len(stacks) != 0:
                new_str.remove('(')
                stacks.pop()
            
            # reverse the string back
            new_str.reverse()
        
        # concat and send
        return "".join(new_str)
                    
            
                
                