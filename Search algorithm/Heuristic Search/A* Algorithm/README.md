# A* Search Algorithm
A* search is the most commonly known form of best-first search. It uses heuristic function h(n), and cost to reach the node n from the start state g(n). It has combined features of UCS and greedy best-first search, by which it solve the problem efficiently. A* search algorithm finds the shortest path through the search space using the heuristic function. This search algorithm expands less search tree and provides optimal result faster. A* algorithm is similar to Best first search except that it uses g(n)+h(n) instead of g(n).
In A* search algorithm, we use search heuristic as well as the cost to reach the node. Hence we can combine both costs as following, and this sum is called as a fitness number.
f(n)= g(n) + h(n).   
Where, h(n)= estimated cost from node n to the goal.

The A* algorithm is implemented by the priority queue.

## A* search algorithm:
1) Place the starting node into the OPEN list.
2) Check if the OPEN list is empty or not, if the list is empty stop and return failure.
3) Remove the node n, from the OPEN list which has the lowest value of f(n), and places it in the CLOSED list, if node n is goal node then return success and stop, otherwise.
4) Expand the node n, and generate the successors of node n, and put n intot the closed list.
5) Check each successor of node n, and find whether any node is a goal node or not. If any successor node is goal node, then return success and terminate the search, else proceed to Step 6.
6)  Else if node n' is already in OPEN and CLOSED, then it should be attached to the back pointer which reflects the lowest g(n') value.
7) Return to Step 2.

## Advantages:
- A* search algorithm is the best algorithm than other search algorithms.
- A* algorithm is optimal and complete.
- This algorithm can solve very complex problems.

## Disadvantages:
- It does not always produce the shortest path as it mostly based on heuristics and approximation.
- A* search algorithm has some complexity issues.
- The main drawback of A* is memory requirement as it keeps all generated nodes in the memory, so it is not practical for various large-scale problems.

## Example:
In this example, we will traverse the given graph using the A* algorithm. The heuristic value of all states is given in the below table so we will calculate the f(n) of each state using the formula f(n)= g(n) + h(n), where g(n) is the cost to reach any node from start state.
Here we will use OPEN and CLOSED list.


![image](https://user-images.githubusercontent.com/101783688/225972662-d6703719-5cdf-4ec1-af4b-13444cc8eb08.png)


#### Time Complexity: 
The worst case time complexity of A* search algorithm is O(b<sup>d</sup>).


#### Space Complexity: 
The worst case space complexity of A* search is O(b<sup>d</sup>).


#### Complete: 
A* algorithm is complete as long as:
- Branching factor is finite.
- Cost at every action is fixed.
#### Optimal: 
A* search algorithm is optimal if it follows below two conditions:

- Admissible: 
The first condition requires for optimality is that h(n) should be an admissible heuristic for A* tree search. An admissible heuristic is optimistic in nature.
- Consistency: Second required condition is consistency for only A* graph-search.
