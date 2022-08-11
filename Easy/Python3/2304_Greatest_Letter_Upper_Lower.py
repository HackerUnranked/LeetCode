# Given a string of English letters s, return the greatest English letter which 
# occurs as both a lowercase and uppercase letter in s. The returned letter 
# should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in 
# the English alphabet. 

# Example 1:

# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.

# Example 2:

# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is 
# greater than 'F' or 'A'.

# Example 3:

# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.

class Solution:
    def greatestLetter(self, s: str) -> str:
        low = [False]*26
        up = [False]* 26
        
        # loop and mark the upper and lower we seen
        for x in s:
            # check if the letter is lowercase and mark it as seen
            # do the same for uppercase
            if ord(x) >= 97:
                low[ord(x) - 97] = True
            else:
                up[ord(x) - 65] = True
        
        # loop backwards and grab the letter that has both upper and lower,
        # note we loop backwards because we want the character with the greatest
        # ascii value that has both upper and lower case appearance
        for a in range(25,-1, -1):
            # found a letter with upper and lower, convert
            # it and return
            if up[a] == True and low[a] == True:
                return chr(a + 65)
            
        return ""