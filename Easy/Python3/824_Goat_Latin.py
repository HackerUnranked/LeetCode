# You are given a string sentence that consist of words separated by spaces. 
# Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language 
# similar to Pig Latin.) The rules of Goat Latin are as follows:

#     If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to 
#     the end of the word.
#         For example, the word "apple" becomes "applema".
#
#     If a word begins with a consonant (i.e., not a vowel), remove the first 
#     letter and append it to the end, then add "ma".
#         For example, the word "goat" becomes "oatgma".
#
#     Add one letter 'a' to the end of each word per its word index in the 
#     sentence, starting with 1.
#         For example, the first word gets "a" added to the end, the second word 
#         gets "aa" added to the end, and so on.

# Return the final sentence representing the conversion from sentence to Goat 
# Latin.

# Example 1:

# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# Example 2:

# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

class Solution:
    def toGoatLatin_split(self, sentence: str) -> str:
        arr = sentence.split(' ') # split the word
        
        # loop each word
        for x in range(len(arr)):
            # if the word starts with a vowel add "ma" to the end
            if (arr[x][0] == 'a' or arr[x][0] == 'e' or arr[x][0] == 'i' or 
                arr[x][0] == 'o' or arr[x][0] == 'u' or arr[x][0] == 'A' or 
                arr[x][0] == 'E' or arr[x][0] == 'I' or arr[x][0] == 'O' or 
                arr[x][0] == 'U'):
                arr[x] += "ma"
            # it's a not a vowel so remove the starting character and
            # at it to the end with ma
            else:
                arr[x] = arr[x][1:] + arr[x][0] + "ma"
            
            # add 'a' equal to the index to the end, we add 1 because idx 0 should
            # be 1
            arr[x] += (x + 1) * 'a'
        
        return " ".join(arr) # create the string and return
    
    # without using split
    def toGoatLatin(self, sentence: str) -> str:
        word = ""
        words = ""
        count = 0
        
        for x, y in enumerate(sentence):
            if y != ' ':
                word += y
            # build the world we hit a space or the end
            if y == ' ' or x == len(sentence) - 1:
                z = word[0] # check the first letter
                if (z == 'a' or z == 'e' or z == 'i' or z == 'o' or z == 'u' or 
                    z == 'A' or z == 'E' or z == 'I' or z == 'O' or z == 'U'):
                    word += "ma" # add ma to the end because we start with a vowel
                else: 
                    # dont start with a vowel, add the first character to the end with ma
                    word = word[1:] + word[0] + 'ma'
                
                word += (count + 1) * 'a' # append a's at the end as many as index is
                    
                # add a space at the end we are not at the last string. the last string
                # doesn't have a space
                if x != len(sentence) - 1:
                    word += ' '
                
                words += word
                word = ""
                count += 1
            
        return words