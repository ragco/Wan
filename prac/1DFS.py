def dfs(node, visited, graph):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited, graph)

# Input graph
graph = {}
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  # undirected

start = int(input("Enter starting node: "))
visited = set()

print("DFS Traversal:", end=' ')
dfs(start, visited, graph)

#input:
#Enter number of edges: 4
#Enter edge (u v): 1 2
#Enter edge (u v): 1 3
#Enter edge (u v): 2 4
#Enter edge (u v): 3 4
#Enter starting node: 1
