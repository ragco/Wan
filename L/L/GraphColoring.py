# Graph Coloring
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

nodes = "abcdef"
node_index = {}

# Map nodes to their indices
for i in range(len(G)):
    node_index[nodes[i]] = i

# Calculate the degree of each node
degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))

colors = ["Blue", "Red", "Yellow", "Green"]
colorDict = {}

# Assign all colors to each node initially
for i in range(len(G)):
    colorDict[nodes[i]] = colors.copy()

# Sort nodes by degree in descending order
sortedNode = []
used_indices = []

for _ in range(len(degree)):
    max_deg = -1
    idx = -1
    for j in range(len(degree)):
        if j not in used_indices and degree[j] > max_deg:
            max_deg = degree[j]
            idx = j
    used_indices.append(idx)
    sortedNode.append(nodes[idx])

# Assign colors to nodes
theSolution = {}
for n in sortedNode:
    current_color = colorDict[n][0]  # pick the first available color
    theSolution[n] = current_color
    # Remove this color from adjacent nodes
    for j in range(len(G[node_index[n]])):
        if G[node_index[n]][j] == 1:
            neighbor = nodes[j]
            if current_color in colorDict[neighbor]:
                colorDict[neighbor].remove(current_color)

# Print the result
print("Node Coloring Result:")
for t in sorted(theSolution):
    print("Node", t, "=", theSolution[t])