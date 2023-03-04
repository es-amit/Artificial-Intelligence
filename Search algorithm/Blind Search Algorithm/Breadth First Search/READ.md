# Breadth First Search
- Breadth-first search is the most common search strategy for traversing a tree or graph. This algorithm searches breadthwise in a tree or graph, so it is called breadth-first search.
- BFS algorithm starts searching from the root node of the tree and expands all successor node at the current level before moving to nodes of next level.
- The breadth-first search algorithm is an example of a general-graph search algorithm.
- Breadth-first search implemented using queue data structure.

### Algorithm
1.  Create a variable called Q and insert the source node into it.
2.  Until a goal state is found or Q is empty.
    1. Remove the first element from Q and call it as E. If Q was empty, quit.
    2. For each way that each rule can match the state described in E do:
        1. Explore all the neighbour vertex of E and insert into Q.
        2. If the goal state found, quit else repeat same steps for other nodes.
3. Return bfs_traversal_output.


### Advantages
- BFS will provide a solution if any solution exists.
- If there are more than one solutions for a given problem, then BFS will provide the minimal solution which requires the least number of steps.

### Disadvantages:

- It requires lots of memory since each level of the tree must be saved into memory to expand the next level.
- BFS needs lots of time if the solution is far away from the root node.

### Example
In the below tree structure, we have shown the traversing of the tree using BFS algorithm from the root node S to goal node K. BFS search algorithm traverse in layers, so it will follow the path which is shown by the dotted arrow, and the traversed path will be:
![image](https://user-images.githubusercontent.com/101783688/222881900-e3178e62-885a-4e05-a45b-0ab020d40bd4.png)

**Time Complexity**: Time Complexity of BFS algorithm can be obtained by the number of nodes traversed in BFS until the shallowest Node. Where the d= depth of shallowest solution and b is a node at every state.

T (b) = O(b<sup>d</sup>)
where, b is branching factor and d is depth

**Space Complexity**: Space complexity of BFS algorithm is given by the Memory size of frontier which is O(b<sup>d</sup>).

**Completeness**: BFS is complete, which means if the shallowest goal node is at some finite depth, then BFS will find a solution.

**Optimality**: BFS is optimal if path cost is a non-decreasing function of the depth of the node.
