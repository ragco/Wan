import heapq

def prim(graph, start_vertex):
    # Number of vertices in the graph
    num_vertices = len(graph)
    
    # To track the MST
    mst = []
    
    # To track the visited vertices
    visited = [False] * num_vertices
    
    # Min-heap to pick the edge with the smallest weight
    min_heap = [(0, start_vertex)]  # (weight, vertex)
    
    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        
        # Skip if the vertex has already been visited
        if visited[vertex]:
            continue
        
        # Mark the vertex as visited
        visited[vertex] = True
        
        # Add the edge to the MST
        mst.append((weight, vertex))
        
        # Check the neighbors of the current vertex
        for neighbor, edge_weight in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    # Return the MST (excluding the initial dummy weight of 0)
    return mst[1:]

def get_input():
    # Get number of vertices and edges from the user
    num_vertices = int(input("Enter the number of vertices: "))
    graph = {i: [] for i in range(num_vertices)}
    
    num_edges = int(input("Enter the number of edges: "))
    
    # Get the edges and weights from the user
    print("Enter each edge in the format: vertex1 vertex2 weight")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Since the graph is undirected
    
    return graph

def main():
    # Get the graph from user input
    graph = get_input()

    # Get the start vertex from the user
    start_vertex = int(input("Enter the starting vertex for Prim's algorithm: "))

    # Run Prim's algorithm
    mst = prim(graph, start_vertex)

    # Display the MST
    print("\nEdges in MST:")
    total_weight = 0
    for weight, vertex in mst:
        print(f"Edge to vertex {vertex} with weight {weight}")
        total_weight += weight
    
    print(f"Total weight of MST: {total_weight}")

if __name__ == "__main__":
    main()
