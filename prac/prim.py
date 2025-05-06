import heapq  

def prims_algorithm(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        if weight != 0:
            mst_edges.append((parent[u], u, weight))

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u
                    heapq.heappush(min_heap, (graph[u][v], v))

    print("\nEdges in MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v}  (Weight: {w})")
    print(f"\nTotal Minimum Cost = {total_cost}")


n = int(input("Enter number of nodes: "))
graph = []

print("Enter adjacency matrix (0 for no edge):")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

key = [float('inf')] * n  # Minimum weight to reach each node
parent = [-1] * n         # Store MST tree
key[0] = 0                # Start from node 0

prims_algorithm (graph,n)