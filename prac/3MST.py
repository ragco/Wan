class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find_parent(self, parent, node):
        while parent[node] != node:
            node = parent[node]
        return node

    def simple_mst(self):
        mst = []
        total_weight = 0
        parent = [i for i in range(self.vertices)]

        # Step 1: Sort all edges by weight (Greedy)
        self.edges.sort()

        # Step 2: Pick edges one by one
        for weight, u, v in self.edges:
            pu = self.find_parent(parent, u)
            pv = self.find_parent(parent, v)

            if pu != pv:  # If adding this edge doesn't form a cycle
                mst.append((u, v, weight))
                total_weight += weight
                parent[pu] = pv  # Union operation

        return mst, total_weight


# Input from user
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))
g = Graph(vertices)

for _ in range(edges):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    g.add_edge(u, v, weight)

# Build and display MST
mst, total_weight = g.simple_mst()

print("\nEdges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v} with weight {weight}")
print(f"\nTotal weight of MST: {total_weight}")
