# Search Algorithms in Artifical Intelligence
Search algorithms are one of the most important areas of Artificial Intelligence. This topic will explain all about the search algorithms in AI.

## Problem-solving agents:
In Artificial Intelligence, Search techniques are universal problem-solving methods. Rational agents or Problem-solving agents in AI mostly used these search strategies or algorithms to solve a specific problem and provide the best result. Problem-solving agents are the goal-based agents and use atomic representation. In this topic, we will learn various problem-solving search algorithms.

## Search Algorithm Terminologies:
- **Search:** Searching is a step by step procedure to solve a search problem in a given search space. A search problem can have three main factors:
    - Search Space: Search space represents a set of possible solutions, which a system may have.
    - Start State: It is a state from where agent begins the search.
    - Goal test: It is a function which observe the current state and returns whether the goal state is achieved or not.
- **Search tree:** A tree representation of search problem is called Search tree. The root of the search tree is the root node which is corresponding to the initial state.
- **Actions:** It gives the description of all the available actions to the agent.
- **Transition model:** A description of what each action do, can be represented as a transition model.
- **Path Cost:** It is a function which assigns a numeric cost to each path.
- **Solution:** It is an action sequence which leads from the start node to the goal node.
- **Optimal Solution:** If a solution has the lowest cost among all solutions.

## Properties of Search Algorithms:
Following are the four essential properties of search algorithms to compare the efficiency of these algorithms:

- **Completeness:** A search algorithm is said to be complete if it guarantees to return a solution if at least any solution exists for any random input.

- **Optimality:** If a solution found for an algorithm is guaranteed to be the best solution (lowest path cost) among all other solutions, then such a solution for is said to be an optimal solution.

- **Time Complexity:** Time complexity is a measure of time for an algorithm to complete its task.

- **Space Complexity:** It is the maximum storage space required at any point during the search, as the complexity of the problem.

## Types of Search algorithms:
Based on the search problems we can classify the search algorithms into uninformed (Blind search) search and informed search (Heuristic search) algorithms.

![image](https://user-images.githubusercontent.com/101783688/222880477-381446e6-78b1-463e-a62d-2430d8c8356d.png)

### Uninformed or Blind search:
The uninformed search does not contain any domain knowledge such as closeness, the location of the goal. It operates in a brute-force way as it only includes information about how to traverse the tree and how to identify leaf and goal nodes. Uninformed search applies a way in which search tree is searched without any information about the search space like initial state operators and test for the goal, so it is also called blind search.It examines each node of the tree until it achieves the goal node.

It can be divided into five main types:
- Breadth-first search
- Uniform cost search
- Depth-first search
- Iterative deepening depth-first search
- Bidirectional Search

### Heuristic or Informed Search
Informed search algorithms use domain knowledge. In an informed search, problem information is available which can guide the search. Informed search strategies can find a solution more efficiently than an uninformed search strategy. Informed search is also called a Heuristic search.

A heuristic is a way which might not always be guaranteed for best solutions but guaranteed to find a good solution in reasonable time.

Informed search can solve much complex problem which could not be solved in another way.

An example of informed search algorithms is 
- Traveling salesman problem.
- Best First Search
- A* Search
- AO* Search
- Hill climbing
