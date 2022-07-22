# There are n pieces arranged in a line, and each piece is colored either by 
# 'A' or by 'B'. You are given a string colors of length n where colors[i] is 
# the color of the ith piece.

# Alice and Bob are playing a game where they take alternating turns removing 
# pieces from the line. In this game, Alice moves first.

# Alice is only allowed to remove a piece colored 'A' if both its neighbors are 
# also colored 'A'. She is not allowed to remove pieces that are colored 'B'.

# Bob is only allowed to remove a piece colored 'B' if both its neighbors are 
# also colored 'B'. He is not allowed to remove pieces that are colored 'A'.

# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other player wins.

# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

# Example 1:

# Input: colors = "AAABABB"
# Output: true
# Explanation:
# AAABABB -> AABABB
# Alice moves first.
# She removes the second 'A' from the left since that is the only 'A' whose 
# neighbors are both 'A'.

# Now it's Bob's turn.
# Bob cannot make a move on his turn since there are no 'B's whose neighbors are 
# both 'B'.
# Thus, Alice wins, so return true.

# Example 2:

# Input: colors = "AA"
# Output: false
# Explanation:
# Alice has her turn first.
# There are only two 'A's and both are on the edge of the line, so she cannot 
# move on her turn.
#Thus, Bob wins, so return false.

# Example 3:

# Input: colors = "ABBBBBBBAAA"
# Output: false
# Explanation:
# ABBBBBBBAAA -> ABBBBBBBAA
# Alice moves first.
# Her only option is to remove the second to last 'A' from the right.

# ABBBBBBBAA -> ABBBBBBAA
# Next is Bob's turn.
# He has many options for which 'B' piece to remove. He can pick any.

# On Alice's second turn, she has no more pieces that she can remove.
# Thus, Bob wins, so return false.

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        bob = 0 # idx char count for bob
        bob1 = 0 # total moves for bob
        alice = 0 # idx char count
        alice1 = 0 # total for moves for alice
        prev = "" # keep track of the previous char
        
        # 1. Keep count of each consecutive character we see for A and B
        # 2. We can make n - 2 moves where n is the number of a consecutive
        #    char that is the same, example n = 5 we can make 3 moves:
        #    AAAAA
        #    AAAA
        #    AAA
        #    AA
        #
        # 3. Everytime the character switches we need to reset the count for the
        #   new character seen
        
        # loop the char in the strings
        for s in colors:
            # base case
            # consecutive matching character
            if prev == "" or prev == s:
                if s == 'A':
                    alice += 1 
                else:
                    bob += 1
            # different character was seen
            else:
                # the previous was B, update B because we seen A
                if s == 'A':
                    if bob > 2:
                        bob1 += bob - 2
                    bob = 0
                    alice = 1 # set alice to 1 because we seen it
                # the previous was A update A because we seen B
                else:
                    if alice > 2:
                        alice1 += alice - 2 
                    alice = 0
                    bob = 1
                    
            prev = s
        
        # special cases where we reach the end and we need
        # to calculate the moves again
        if bob > 2:
            bob1 += bob - 2
        
        if alice > 2:
            alice1 += alice - 2
        
        # alice loses if AA is the longest substring because she
        # is making the first move
        if alice1 == 0:
            return False
        # same as alice, bob loses if he can't make a move
        if bob1 == 0:
            return True
        
        # alice loses if they have the same length substring
        #
        # AAABBB
        # AABBB
        # AABB
        # bob wins because alice cannot make a move since she has to go first
        # therefore she will have 1 less move to make towards the end making
        # here the loser
        if alice1 == bob1:
            return False
        # alice wins if she has more moves
        if alice1 > bob1:
            return True
        else:
            return False