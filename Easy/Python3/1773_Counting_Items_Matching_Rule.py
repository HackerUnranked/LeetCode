from typing import List

# You are given an array items, where each items[i] = [typei, colori, namei]
#  describes the type, color, and name of the ith item. You are also given a 
# rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

#    ruleKey == "type" and ruleValue == typei.
#     ruleKey == "color" and ruleValue == colori.
 #    ruleKey == "name" and ruleValue == namei.

# Return the number of items that match the given rule.

# Example 1:

# Input: items = [["phone","blue","pixel"],
#                 ["computer","silver","lenovo"],
#                 ["phone","gold","iphone"]],
#                 ruleKey = "color",
#                 ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

# Example 2:

# Input: items = [["phone","blue","pixel"],
#                 ["computer","silver","phone"],
#                 ["phone","gold","iphone"]],
#                 ruleKey = "type",
#                 ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule,
#              which are ["phone","blue","pixel"] and ["phone","gold","iphone"].

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        idx = 0

        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2

        sums = 0

        for things in items:
            if things[idx] == ruleValue:
                sums += 1
        
        return sums
