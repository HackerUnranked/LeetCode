from typing import List

# Given an array of strings words, return the words that can be typed using 
# letters of the alphabet on only one row of American keyboard like the image 
# below.

# In the American keyboard:

#     the first row consists of the characters "qwertyuiop",
#     the second row consists of the characters "asdfghjkl", and
#     the third row consists of the characters "zxcvbnm". 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

# Example 2:

# Input: words = ["omk"]
# Output: []

# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # create set of the rows for the keyboard
        arr = [ set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm") ]
        d = [] # the array we are returning
        
        # loop the words
        for word in words:
            
            row = 0 # keeps track of the row we checking on the keyboard
            found = True # flag if the letter is on the same row
            
            # loop the characters in the word
            for a in word:
                
                a = a.lower() # make the character lowercase because we have 
                              # upper and lowercase in the string 
                
                # find the row we are looking at
                if row == 0:
                    if a in arr[0]:
                        row = 1
                    elif a in arr[1]:
                        row = 2
                    elif a in arr[2]:
                        row = 3
                # check if the letter is in the corresponding row
                else:
                    if row == 1:
                         if a not in arr[0]:
                            found = False
                            break
                    if row == 2:
                        if a not in arr[1]:
                            found = False
                            break
                    if row == 3:
                        if a not in arr[2]:
                            found = False
                            break
            # append the word if all the letters were found on one row
            if found == True:
                d.append(word)
        
        return d