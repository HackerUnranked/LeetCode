# Given a string s and a character letter, return the percentage of characters 
# in s that equal letter rounded down to the nearest whole percent. 

# Example 1:

# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% 
# when rounded down, so we return 33.

# Example 2:

# Input: s = "jjjj", letter = "k"
# Output: 0
# Explanation:
# The percentage of characters in s that equal the letter 'k' is 0%, so we 
# return 0.

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        count = 0
        # count the occurence of the character
        for x in s:
            if x == letter:
                count += 1
        
        # find the percentage then mulitply if by 100
        # to get it as a whole percent
        return int(count / len(s) * 100)