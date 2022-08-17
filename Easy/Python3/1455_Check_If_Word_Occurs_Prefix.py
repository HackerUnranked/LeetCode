# Given a sentence that consists of some words separated by a single space, and 
# a searchWord, check if searchWord is a prefix of any word in sentence.

# Return the index of the word in sentence (1-indexed) where searchWord is a 
# prefix of this word. If searchWord is a prefix of more than one word, return 
# the index of the first word (minimum index). If there is no such word return 
# -1.

# A prefix of a string s is any leading contiguous substring of s.

# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the 
# sentence.

# Example 2:

# Input: sentence = "this problem is an easy problem", searchWord = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in 
# the sentence, but we return 2 as it's the minimal index.

# Example 3:

# Input: sentence = "i am tired", searchWord = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w = ""
        count = 0
        
        for idx in range(len(sentence)):
            # add the letter if we are not a space and we are not
            # equal to the prefix len
            if sentence[idx] != ' ' and len(w) != len(searchWord):
                w += sentence[idx]
            
            # we found a match
            if len(w) == len(searchWord) and w == searchWord:
                return count + 1 # incrememnt count because we are the ith word
            
            # we are at the end of a word incrememnt the count to
            # keep track of how many words we seen and reset the string
            if idx == len(sentence) - 1 or sentence[idx] == ' ':
                count += 1
                w = ""
        
        return -1 # return negative one because there is no such string
    
    def isPrefixOfWord_split(self, sentence: str, searchWord: str) -> int:
        
        # using string split method
        for idx, word in enumerate(sentence.split(' ')):
            if len(word) >= len(searchWord) and word[0:len(searchWord)] == searchWord:
                return idx + 1
        
        return -1