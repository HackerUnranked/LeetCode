from typing import List

# Given a list of strings words and a string pattern, return a list of words[i] 
# that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that 
# after replacing every letter x in the pattern with p(x), we get the desired 
# word.

# Recall that a permutation of letters is a bijection from letters to letters: 
# every letter maps to another letter, and no two letters map to the same letter.

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation 
# {a -> m, b -> e, ...}. 
# 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a 
# permutation, since a and b map to the same letter.

# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        
        for word in words:
            dic = [-1] * 26 # matches a pattern letter to a word letter
            uniq = [-1] * 26 # keeps track of all the word letter we seen
            found = True # checks to see if we have a matching pattern
            
            # map the pattern to a letter from the word
            for idx in range(len(word)):
                p_val = ord(pattern[idx]) -  97
                w_val = ord(word[idx]) - 97
                
                # the pattern has not been mapped
                if dic[p_val] == -1:
                    # the word letter has not been mapped either
                    if uniq[w_val] == -1:
                        dic[p_val] = w_val # map the two together
                        uniq[w_val] = True # add as we seen the key value
                    # we already mapped the pattern to a letter
                    # leave as this means they don't share the same pattern
                    else:
                        found = False
                        break
                # check if the pattern matches the letter in word and leave if
                # they don't match
                elif dic[p_val] != w_val:
                    found = False
                    break
                
            # we have a match, add the word to the answer
            if found == True:
                ans.append(word)
        
        return ans