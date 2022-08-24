from typing import List

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find 
# all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit 
# from node i (i.e., there is a directed edge from node i to node graph[i][j]). 

# Example 1:

# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Example 2:

# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        destination = len(graph) - 1
        
        def dfs(idx_node, path, output):
            # if we reached the destination node which is the last node in the graph
            # append it to the output
            if idx_node == destination:
                output.append(path)
            
            # loop all the paths that the current
            # node can reach and call dfs
            for next_node in graph[idx_node]:
                # from our current node see where the next node takes us.
                # the second arguement adds the path we are already at
                # and appends the next node to it because it is the path
                dfs(next_node, path + [next_node], output)
            
        output = [] # holds the paths that can reach the last node
        dfs(0, [0], output) # pass node zero because we only care about starting at node zero
        
        return output