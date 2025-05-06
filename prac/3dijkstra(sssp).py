import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# --------- User Input Section ---------
graph = {}
n = int(input("Enter number of vertices: "))
print("Enter vertex names:")
vertices = [input(f"Vertex {i+1}: ") for i in range(n)]

# Initialize graph dictionary
for vertex in vertices:
    graph[vertex] = []

e = int(input("Enter number of edges: "))
print("Enter edges in format: from to weight")
for _ in range(e):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))  # Remove this line if graph is directed

start = input("Enter the starting vertex: ")

# Run Dijkstra
shortest_distances = dijkstra(graph, start)

# --------- Output ---------
print("\nShortest distances from", start)
for vertex in vertices:
    print(f"{start} -> {vertex} = {shortest_distances[vertex]}")

# Enter number of vertices:  4
# Enter vertex names:
# Vertex 1:  A
# Vertex 2:  B
# Vertex 3:  C
# Vertex 4:  D
# Enter number of edges:  5
# Enter edges in format: from to weight
#  A B 20
#  B C 10
#  A C 5
#  A D 33
#  D C 66
# Enter the starting vertex:  A

# Shortest distances from A
# A -> A = 0
# A -> B = 15
# A -> C = 5
# A -> D = 33
