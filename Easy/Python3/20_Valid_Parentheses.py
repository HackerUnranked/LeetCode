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
    
    # Same solution but a more readable way
    def isValid_v2(self, s: str) -> bool:
        if len(s) == 0:
            return False
        
        stack = []
        set_open = {'(', '[', '{'}
        set_match_open = {']':'[', '}':'{', ')':'('}
        
        for a in s:
            if a in set_open:
                stack.append(a)
            else:
                if len(stack) == 0:
                    return False
                elif set_match_open[a] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        return False
'''
Same solution as above but written a different way

class Solution:
    def isValid(self, s: str) -> bool:
        parans = []
        for x in s:
            # push all the openning parans first
            if x == '{' or x == '(' or x == '[':
                parans.append(x)
            # we received a closing parans
            else:
                # if the list is empty return false because
                # we don't have a matching open parans
                if parans == []:
                    return False
                # check to see if the open parans match the
                # last closing parans that we received
                else:
                    if x == '}':
                        # we have a match remove the matching pair
                        if parans[-1] == '{':
                            parans.pop()
                        else:
                            return False
                    if x == ")":
                        if parans[-1] == '(':
                            parans.pop()
                        else:
                            return False
                    if x == ']':
                        if parans[-1] == '[':
                            parans.pop()
                        else:
                            return False
        if parans != []:
            return False
        return True
'''                             