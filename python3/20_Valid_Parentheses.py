#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
 

#Example 1:

#Input: s = "()"
#Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for x in s:
            if x == '[' or x == '(' or x == '{':
                stack.append(x)
            if x == ']' or x == ')' or x == '}':
                if not stack:
                    return False
                elif stack[-1] == '[' and x != ']':
                    return False
                elif stack[-1] == '(' and x != ')':
                    return False
                elif stack[-1] == '{' and x != '}':
                    return False
                else:
                    stack.pop()
        
        if not stack:
            return True
        else:
            return False
                
                
            