# Set a large number to represent infinity
INF = 9999999

# Number of vertices in the graph
N = 5

# Creating the graph using an adjacency matrix
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

# Keep track of which nodes are selected in the MST
selected_node = [0, 0, 0, 0, 0]

# Keep track of the number of edges added to the MST
no_edge = 0

# Initially, mark the first node as selected
selected_node[0] = True

# Print the header for the output
print("Edge : Weight\n")

# Continue until all vertices are included in the MST
while(no_edge < N - 1):
    # Initialize minimum weight to infinity
    minimum = INF
    a = 0
    b = 0
    # Iterate over each selected node
    for m in range(N):
        if selected_node[m]:
            # Iterate over each unselected node adjacent to the selected node
            for n in range(N):
                if((not selected_node[n]) and G[m][n]):
                    # If the weight of the edge is less than the current minimum, update minimum and store the vertices
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    # Print the edge and its weight
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    # Mark the newly connected node as selected
    selected_node[b] = True
    # Increment the count of edges added
    no_edge += 1


#Prim's Algorithm (Minimum Spanning Tree)

#1. Initialize an empty set mstSet to keep track of vertices included in the MST.
#2. Initialize an array key[] to store the key values (minimum edge weight) of each vertex. Initialize all key values to positive infinity.
#3. Initialize an array parent[] to store the parent vertex of each vertex in the MST. Initialize all parent values to -1.
#4. Choose an arbitrary starting vertex and set its key value to 0.
#5. Loop while mstSet doesn't include all vertices:
#      a. Extract the vertex u with the minimum key value from the set of vertices not in mstSet.
#      b. Add u to mstSet.
#      c. For each vertex v adjacent to u:
#           i. If v is not in mstSet and the weight of edge (u, v) is less than the current key value of v:
#               - Update the key value of v to the weight of edge (u, v).
#                - Update the parent of v to u.
#6. The resulting set of edges forms the Minimum Spanning Tree.


