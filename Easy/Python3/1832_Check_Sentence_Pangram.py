# A pangram is a sentence where every letter of the English alphabet appears at 
# least once.

# Given a string sentence containing only lowercase English letters, return true
# if sentence is a pangram, or false otherwise. 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English 
# alphabet.

# Example 2:

# Input: sentence = "leetcode"
# Output: false
 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        bit = 0
        
        # loop each character in the sentence
        for x in sentence:
            # shift right b x place and flip the bit
            a = 1 << (ord(x) - 97) 
            bit |= a # mark it if we already seen it
        
        if bit + 1 == 2**26: # return true if all the bits are set
            return True
        else:
            return False
        