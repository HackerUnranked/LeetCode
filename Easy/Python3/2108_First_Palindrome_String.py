from typing import List

# Given an array of strings words, return the first palindromic string in the 
# array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:

# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:

# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # loop through the words
        for word in words:
            # if the word matches the reverse then it
            # is a palindrome and return it
            if word[::-1] == word:
                return word
        
        return "" # we didn't find a palindrome
    
    # using loop instead of string slice
    def firstPalindrome_2(self, words: List[str]) -> str:
        # loop through the words
        for word in words:
            # if the word matches the reverse then it
            # is a palindrome and return it
            start = 0
            end = len(word) - 1
            found = True
            
            # loop the idx of the string from the beginning and end
            # up until the middle and check if the characters match
            while start < end:
                # the letters don't match, not a palindrome
                if word[start] != word[end]:
                    found = False
                    break
                else:
                    start += 1
                    end -= 1
                    
            if found == True:
                return word
        
        return "" # we didn't find a palindrome