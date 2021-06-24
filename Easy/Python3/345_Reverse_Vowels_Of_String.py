# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

#Example 1:
 
# Input: s = "hello"
# Output: "holle"

# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        right = 0
        left =  len(s)
        s = list(s)
        if s == 1:
            return s
        else:
            while (right < len(s)) and (left > 0) and (right < left):
                if self.is_vowel(s[right]):
                    if self.is_vowel(s[left-1]):
                        temp_right = s[right]
                        s[right] = s[left-1]
                        s[left -1] = temp_right
                        # if both are vowels then i move the index
                        right += 1
                        left -= 1
                    # only the right is a vowel, move the left index
                    else:
                        left -= 1
                # the right is not a vowel, do we need to move the left also?
                else:
                    if self.is_vowel(s[left-1]):
                        right += 1
                    # both are not vowels
                    else:
                        right += 1
                        left -= 1
                        
            new_str = ""
            return new_str.join(s)
        
    def is_vowel (self, letter):
        good = False;
                
        if letter == 'A':
            good = True
        elif letter == 'a':
            good = True
        elif letter == 'E':
            good = True
        elif letter == 'e':
            good = True
        elif letter == 'I':
            good = True
        elif letter == 'i':
            good = True
        elif letter == 'O':
            good = True
        elif letter == 'o':
            good = True
        elif letter == 'U':
            good = True
        elif letter == 'u':
            good = True
                    
        return good