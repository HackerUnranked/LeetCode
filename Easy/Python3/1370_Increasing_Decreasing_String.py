# given a string X with n characters, create a string using letters from X where 
# the string is ascedning in value then decreasing, repeat this occurence.

# example 1: 
# X = aabbcc
# answer = abccba where abc ascending and cba descending
#
# example 2:
#
# X = cacbbcaba
# answer = abccbaabc, abc increasing, cba decreasing then abc increasing again


class Solution:
    def sortString(self, s: str) -> str:
        
        buckets = [0]*26 # bucket to count each letter
        
        # count the occurence of each letter
        for x in s:
            buckets[ord(x) - 97] += 1
        
        b = "" # string to create
        
        # loop while the length are different
        while len(b)!= len(s):
            
            # build the ascending portion of the string first
            for idx, val in enumerate(buckets):
                if val != 0:
                    b += chr(idx + 97) # convert to char
                    buckets[idx] -= 1 # subtract from bucket
            
            # loop the string backwards to get descending string
            for idx2 in range(len(buckets)-1, -1, -1):
                if buckets[idx2] != 0:
                    b += chr(idx2 + 97)
                    buckets[idx2] -= 1
        
        return b # return the string