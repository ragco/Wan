class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False


def kruskal_algorithm(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    ds = DisjointSet(vertices)

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost


# ----------- MAIN PROGRAM -------------
print("Kruskal's Minimum Spanning Tree Algorithm")

# Input vertices
n = int(input("Enter number of vertices: "))
vertices = []
print("Enter the vertex names:")
for _ in range(n):
    vertices.append(input().strip())

# Input edges
e = int(input("Enter number of edges: "))
edges = []
print("Enter each edge in the format: vertex1 vertex2 weight")
for _ in range(e):
    u, v, w = input().split()
    edges.append((u, v, int(w)))

# Run Kruskal's algorithm
mst, cost = kruskal_algorithm(vertices, edges)

# Output
print("\nEdges in Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")
print("Total cost of MST:", cost)

# Kruskal's Minimum Spanning Tree Algorithm

# Enter number of vertices:  4
# Enter the vertex names:
#  a
#  b
#  c
#  d
# Enter number of edges:  5
# Enter each edge in the format: vertex1 vertex2 weight
#  a b 5
#  b c 7 
#  a d 8
#  c d 2
#  d a 2

# Edges in Minimum Spanning Tree:
# c - d : 2
# d - a : 2
# a - b : 5
# Total cost of MST: 9