# You are given a string s of even length. Split this string into two halves of 
# equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains 
# uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore
# , they are alike.

# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. 
# Therefore, they are not alike.
# Notice that the vowel o is counted twice.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def count_vowels(word):
            
            idx = 0
            num = 0
            
            # loop the string and check if it's a vowel then count it
            while idx < len(word):
                c = word[idx].lower() # lower case sense we have both upper and lower chars
                if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                    num += 1
                
                idx += 1
            
            return num
        
        # if the count is the same, they have the same num vowels and return true
        if count_vowels(s[0:len(s) // 2]) == count_vowels(s[len(s) // 2:]):
            return True
        else:
            return False # return false they have different count