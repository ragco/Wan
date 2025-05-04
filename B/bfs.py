from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Take input
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

# Initialize graph
graph = {i: [] for i in range(vertices)}

print("Enter edges (format: src dest):")
for _ in range(edges):
    u, v = map(int, input().split())
    if u not in graph or v not in graph:
        print(f"Invalid edge: {u} {v} — vertex out of bounds.")
        continue
    graph[u].append(v)
    graph[v].append(u)  # Because the graph is undirected

# Get starting node
start = int(input("Enter starting vertex: "))

# Perform BFS
print("BFS Traversal:")
bfs(graph, start)
