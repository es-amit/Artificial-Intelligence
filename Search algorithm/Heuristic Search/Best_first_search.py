from queue import PriorityQueue
def best_first_search(graph,start,goal):
    open = PriorityQueue()
    closed = list()
    bfs_traversal_output = list()
    open.put(start)
    while not open.empty():
        node = (open.get())[1]
        closed.append(node)
        bfs_traversal_output.append(node)
        if node == goal[1]:
            break
        else:
            for v in graph[node]:
                if v[1] not in closed:
                    open.put(v)

    return bfs_traversal_output


graph={
    'A':[(32,'B'),(25,'C'),(35,'D')],
    'B': [(40,'A'),(19,'E')],
    'C': [(40,'A'),(19,'E'),(17,'F')],
    'D': [(40,'A'),(17,'F')],
    'E': [(32,'B'),(25,'C'),(10,'H')],
    'F': [(25,'C'),(35,'D'),(0,'G')],
    'G': [(17,'F'),(10,'H')],
    'H': [(19,'E'),(0,'G')]
}

start = (40,'A')
goal = (0,'G')

print("Path:",best_first_search(graph,start,goal))
