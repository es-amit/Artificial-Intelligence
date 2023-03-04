from queue import Queue
#Graph Representation
adj_list={
    1:[2,4],
    2:[1,5,7,8,3],
    3:[2,4,9,10],
    4:[1,3],
    5:[2,7,8,6],
    6:[5],
    7:[2,5,8],
    8:[2,5,7],
    9:[3],
    10:[3]
}

visited={}                    #Record the vertices, whether they are visited or not 
level={}                      #Record the minimum distance from source node to goal node 
parent={}                     #Record all the vertices with their parent
bfs_traversal_output=[]
queue=Queue()

#Initialisation
for node in adj_list.keys():
    visited[node]= False        #All the vertices are initially unvisited
    level[node]= -1             #All vertices has distance -1 or infinity.
    parent[node]= None          #vertices has no parent


source=int(input("Enter the Source Node:"))
visited[source]=True            #Source vertice is set to visited
level[source]=0                 #Level of source vertex is zero
queue.put(source)               #Inserting source vertex into Queue

while not queue.empty():
    u=queue.get()               #Removing first element from the Queue and giving value to u variable
    bfs_traversal_output.append(u)    
    for v in adj_list[u]:         #Visiting all the neighbour vertices of u vertex
        if not visited[v]:
            visited[v]=True
            level[v]=level[u]+1
            parent[v]=u
            queue.put(v)          #Inserting vertex into the queue

print("BFS Traversal:",bfs_traversal_output)


#Shortest distance from source to vertice
vertice=int(input("Enter the Goal node:"))
goal=vertice
print(f"The shortest distance from {source} to {vertice}: {level[vertice]}")

#shortest path from source to vertice
path=[]
while vertice is not None:
    path.append(vertice)
    vertice = parent[vertice]
path.reverse()
print(f"The path from {source} to {goal} : {path}")


"""OUTPUT:
Enter the Source Node:1
BFS Traversal: [1, 2, 4, 5, 7, 8, 3, 6, 9, 10]
Enter the Goal node:10
The shortest distance from 1 to 10: 3
The path from 1 to 10 : [1, 2, 3, 10]
"""
