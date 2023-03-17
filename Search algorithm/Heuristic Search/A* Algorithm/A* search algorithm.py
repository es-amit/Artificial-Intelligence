from queue import PriorityQueue

def a_star(graph,start,goal,heuristic):
    # Initialize the open and closed sets
    open_set = PriorityQueue()
    open_set.put((0,start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    # Loop until goal is reached or open set is empty
    while not open_set.empty():
        # Get the node with the lowest f-score from the open set
        current = open_set.get()[1]

        # If goal is reached, return the path
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Explore neighbors of current node
        for neighbor in graph[current]:
            # Calculate the cost of the path to the neighbor
            new_cost = cost_so_far[current] + graph[current][neighbor]
            # Update the cost of the path if it is lower than the current cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                # Calculate the f-score of the neighbor (g-score + heuristic)
                priority = new_cost + heuristic[neighbor]
                # Add the neighbor to the open set with its f-score as priority
                open_set.put((priority,neighbor))
                came_from[neighbor] = current

    # If the goal cannot be reached, return None
    return None




if __name__ == "__main__":
    # Graph representation, keys are the nodes and  the values are the neighbours with their cost
    graph = {
        'S': {'C': 3,'B': 4},
        'B': {'S': 4,'F': 5,'E': 12},
        'C': {'S': 2,'D': 7,'E': 10},
        'D': {'C': 7,'E': 2},
        'E': {'B': 12,'C': 10,'D': 2,'G': 5},
        'F': {'B': 5,'G': 16},
        'G': {'E': 5,'F': 16}
    }
    # It is heuristic function which is given
    heuristic = {
        'S': 14,
        'B': 12,
        'C': 11,
        'D': 6,
        'E': 4,
        'F': 11,
        'G': 0,
    }

    start = 'S'
    goal = 'G'
    path = a_star(graph,start,goal,heuristic)
    print(path)
    
    
    '''Output:
    ['S', 'C', 'D', 'E', 'G']
    '''
