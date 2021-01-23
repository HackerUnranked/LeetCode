# You are given an integer n, the number of teams in a tournament that has strange rules:
# If the current number of teams is even, each team gets paired with another team.
# A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament, 
# and the rest gets paired. A total of (n - 1) / 2 matches are played, and
# (n - 1) / 2 + 1 teams advance to the next round.

# Return the number of matches played in the tournament until a winner is decided. 

# Example 1:

# Input: n = 7
# Output: 6
# Explanation: Details of the tournament: 
# - 1st Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 2nd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 3rd Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 3 + 2 + 1 = 6.

# Example 2:

# Input: n = 14
# Output: 13
# Explanation: Details of the tournament:
# - 1st Round: Teams = 14, Matches = 7, and 7 teams advance.
# - 2nd Round: Teams = 7, Matches = 3, and 4 teams advance.
# - 3rd Round: Teams = 4, Matches = 2, and 2 teams advance.
# - 4th Round: Teams = 2, Matches = 1, and 1 team is declared the winner.
# Total number of matches = 7 + 3 + 2 + 1 = 13.

class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        rounds = 0
        while n != 1:
            
            #if its even we divide by 2 to get the number if pairs aka matches
            if n%2 == 0:
                n //= 2
                rounds += n
            # if its odd we subtract 1 to get an even number
            # divide by 2 to get the number of matches aka matches
            # add 1 to account for the team that moves on
            else:
                n = n - 1
                n //=2
                rounds = rounds + n + 1
                
        return rounds
                