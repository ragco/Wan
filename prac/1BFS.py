from collections import deque

def bfs_recursive(queue, visited, graph):
    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    bfs_recursive(queue, visited, graph)

# Input graph
graph = {} #dict[int, list[int]]
num_edges = int(input("Enter number of edges: "))
for _ in range(num_edges):#This loop runs num_edges times → you’re just #using it to repeat an action (taking edge input), but You don’t need the #index 0,1,2
    u, v = map(int, input("Enter edge (u v): ").split())
    graph.setdefault(u, []).append(v) #graph[u] = [v]
    graph.setdefault(v, []).append(u)  # undirected

start = int(input("Enter starting node: "))
visited = set()
queue = deque([start])

print("BFS Traversal:", end=' ')
bfs_recursive(queue, visited, graph)

#input:
#Enter number of edges: 4
#Enter edge (u v): 1 2
#Enter edge (u v): 1 3
#Enter edge (u v): 2 4
#Enter edge (u v): 3 4
#Enter starting node: 1
