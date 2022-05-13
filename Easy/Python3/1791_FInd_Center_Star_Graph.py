from typing import List

# There is an undirected star graph consisting of n nodes labeled from 1 to n. 
# A star graph is a graph where there is one center node and exactly n - 1 edges
# that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] 
# indicates that there is an edge between the nodes ui and vi. 
# Return the center of the given star graph.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # since the node is a star it means all the other nodes
        # share 1 of of the same node that they point back to
        # this means each edge contains the center node
        # we just need to check which one of the nodes in the first edge is 
        # also in the second edge, this means it's the center node because
        # it's in both
        
        # is the first node in the first edge the same as either node in the second edge?
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        
        return edges[0][1]