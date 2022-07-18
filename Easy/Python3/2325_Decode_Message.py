# You are given the strings key and message, which represent a cipher key and a 
# secret message, respectively. The steps to decode message are as follows:

#     Use the first appearance of all 26 lowercase English letters in key as the
#     order of the substitution table.
#    
#     Align the substitution table with the regular English alphabet.
#     Each letter in message is then substituted using the table.
#     Spaces ' ' are transformed to themselves.

#     For example, given key = "happy boy" (actual key would have at least one 
#     instance of each letter in the alphabet), we have the partial substitution
#      table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

# Return the decoded message.

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        buckets = [-1]*26 # map each letter to this array
        idx = 97 # ascii value starting point, 97 = a
        
        # create a mapping
        for letter in key:
            # if this is not a whitespace and we haven't seen the letter yet, create a mapping
            if letter != ' ' and buckets[122 - ord(letter)] == -1:
                buckets[122 - ord(letter)] = idx # set the ascii value of the character equal to idx
                idx += 1 # move idx over one to move forward in the alphabet
                
        word = "" # where we will store the word
        
        # loop through the message
        for letter in message:
            if letter == ' ': # if it is a whitespace just concat
                word += " "
            else:
                word += chr(buckets[122 - ord(letter)]) # calculate what letter it is using the mapping in bucket and concat
        
        return word