time=0
def DFS(adj_list,source):
    global time
    color[source]='G'                                             # let take source vertex currently visiting
    time_trav[source][0]=time                                     #starting time traversal of source node
    dfs_traversal_output.append(source)                           # adding source node to the dfs traversal output variable 
    for v in adj_list[source]:                                    # exploring the neighbour node of source
        if color[v] == 'W':
            parent[v]=source
            DFS(adj_list,v)                                       #calling recursively the function with neighbour nodes
    color[source]="B"                                             # marking visited node 
    time_trav[source][1]=time                                     
    time+=1
    return dfs_traversal_output


adj_list={'A': ['B', 'C'],                                              #graph
          'B': ['A', 'D'],
          'C': ['A', 'D', 'E'],
          'D': ['B', 'C', 'E'],
          'E': ['C', 'D']}          
color=dict()                                                        # if the node is white then it is unvisited, black for visited, Grey for currently visiting
parent={}                                                           # save who is parent of whom node
time_trav=dict()                                                    # it tracks the node visiting time of all node, every visiting node will increase by 1
dfs_traversal_output=[]
for u in adj_list.keys():
    color[u]='W'                                                    #all the nodes are unvisited
    parent[u]=None                                                  # No one is parent of other node
    time_trav[u]=[-1,-1]                                            # currently no vertices are visiting

print(DFS(adj_list,'A'))

"""Output
['A', 'B', 'D', 'C', 'E']
"""
