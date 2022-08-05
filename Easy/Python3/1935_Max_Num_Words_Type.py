# There is a malfunctioning keyboard where some letter keys do not work. All 
# other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or 
# trailing spaces) and a string brokenLetters of all distinct letter keys that 
# are broken, return the number of words in text you can fully type using this 
# keyboard. 

# Example 1:

# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.

# Example 2:

# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

# Example 3:

# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken. 

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bucket = [False] * 26
        
        # mark the letters we seen as true
        for a in brokenLetters:
            bucket[ord(a) - 97] = True
        
        skip = False
        word_count = 0
        
        for x in range(len(text)):
            # we reached a space, this means
            # we start a new word
            if text[x] == ' ':
                # this was a bad word, set skip to False because
                # we are starting to check a new word
                if skip == True:
                    skip = False
                # the word was good so increment the count
                else:
                    word_count += 1
            else:
                # we check the letter because the word is still good
                if skip == False:
                    # if the letter we are looking at is one of the
                    # bad ones then we need to start skipping
                    if bucket[ord(text[x]) - 97] == True:
                        skip = True
                    # the letter is good, we need to check if we are at the end of the string
                    # because it has no space at the end and we want to check add the string if
                    # it is good
                    else:
                        if x == len(text) - 1:
                            word_count += 1
                        
        
        return word_count
    
    # another way but using string split
    def canBeTypedWords_split(self, text: str, brokenLetters: str) -> int:
        a = text.split(' ') # split the string into words
        word = 0 # count the words
        
        # loop each word
        for x in a:
            found = False
            # check if the letters in broke letters is in the word
            for b in brokenLetters:
                if b in x:
                    found = True
                    break
                    
            if found == False:
                word += 1
        
        return word