class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # Graph will be stored as a list of edges

    # Function to add an edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []  # Store the resultant MST
        i = 0        # Index for sorted edges
        e = 0        # Index for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree cost:", minimumCost)

# ✔️ Input Section (Only this part is changed)
if __name__ == '__main__':
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    g = Graph(V)
    print("Enter each edge in the format: u v w")

    for i in range(E):
        u, v, w = map(int, input(f"Edge {i + 1}: ").split())
        g.addEdge(u, v, w)

    g.KruskalMST()