from typing import List

# Every valid email consists of a local name and a domain name, separated by the '@' sign. 
# Besides lowercase letters, the email may contain one or more '.' or '+'.
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. 
# Note that this rule does not apply to domain names.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. 
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".

# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        the_set = set()
        nums = 0
        
        for x in emails:
            # split the list on the domain
            b = x.split("@")
            
            # replace the local name of dots
            b[0] = b[0].replace(".","")
            
            # check if ther is a plus in the local name, if there is,
            # we need to ignore it
            if "+" in b[0]:
                to_find = b[0].find('+')
                bob = b[0]
                b[0] = bob[0:to_find]
            
            x = str(b[0]) +"@"+str(b[1])
            
            if x not in the_set:
                
                nums += 1
                the_set.add(x)
        
        return nums
            