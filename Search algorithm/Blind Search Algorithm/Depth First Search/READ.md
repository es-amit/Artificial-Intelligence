# Depth First Search
- The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. 
So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them. Finally, print the nodes in the path.
- Breadth-first search implemented using stack(recursion) data structure.

### Algorithm
1.  Create a recursive function that takes the index of the node and a visited array.
2. Mark the current node as visited and print the node.
3. Traverse all the adjacent and unmarked nodes and call the recursive function with the index of the adjacent node.
4. Run a loop from 0 to the number of vertices and check if the node is unvisited in the previous DFS, then call the recursive function with the current node.


### Advantages
- Memory requirement is only linear with respect to the search graph. This is in contrast with breadth-first search which requires more space. The reason is that the algorithm only needs to store a stack of nodes on the path from the root to the current node.
- The time complexity of a depth-first Search to depth d is O(bd) since it generates the same set of nodes as breadth-first search, but simply in a different order. Thus practically depth-first search is time-limited rather than space-limited.
- If depth-first search finds solution without exploring much in a path then the time and space it takes will be very less.
- DFS requires less memory since only the nodes on the current path are stored. By chance DFS may find a solution without examining much of the search space at all.

### Disadvantages:

- The disadvantage of Depth-First Search is that there is a possibility that it may down the left-most path forever. Even a finite graph can generate an infinite tre One solution to this problem is to impose a cutoff depth on the search. Although ideal cutoff is the solution depth d and this value is rarely known in advance of actually solving the problem. If the chosen cutoff depth is less than d, the algorithm will fail to find a solution, whereas if the cutoff depth is greater than d, a large price is paid in execution time, and the first solution found may not be an optimal one.
- Depth-First Search is not guaranteed to find the solution.
- there is no guarantee to find a minimal solution, if more than one solution.

### Example
In the below tree structure, we have shown the traversing of the tree using DFS algorithm from the root node S to goal node J. DFS search algorithm traverse in levels(depth), so it will follow the path which is shown by the dotted arrow, and the traversed path will be:
![image](https://user-images.githubusercontent.com/101783688/224468820-f257aa6b-d8b3-4d6f-9281-ff7a73d6689e.png)

**Time Complexity**: Time Complexity of DFS algorithm can be

T (b) = O(b<sup>d</sup>)
where, b is branching factor and d is depth

**Space Complexity**: Space complexity of DFS algorithm is given by the Memory size of frontier which is O(b<sup>d</sup>).

**Completeness**: DFS is not complete, which means if the goal node is at some finite depth, then DFS may or may not find a solution.
