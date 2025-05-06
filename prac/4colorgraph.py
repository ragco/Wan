def is_safe(node, color, graph, colors):
    # Check if any adjacent node has the same color
    for adj in range(len(graph)):
        if graph[node][adj] == 1 and colors[adj] == color:
            return False
    return True

def backtrack(graph, m, colors, node=0):
    if node == len(graph):
        return True  # All nodes are colored

    for c in range(1, m + 1):  # Try all colors
        if is_safe(node, c, graph, colors):
            colors[node] = c
            if backtrack(graph, m, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack

    return False  # No valid color found

# --- Input & Execution ---
print("Enter number of nodes: ")
n = int(input())
print("Enter number of colors: ")
m = int(input())

print("Enter adjacency matrix (0/1):")
graph = [list(map(int, input().split())) for _ in range(n)]

colors = [0] * n
if backtrack(graph, m, colors):
    print("Coloring possible:", colors)
else:
    print("No solution exists with", m, "colors.")

# def is_safe(node, color, graph, colors):
#     return all(graph[node][i] == 0 or colors[i] != color for i in range(len(graph)))

# def backtrack(graph, m, colors, node=0):
#     if node == len(graph): return True
#     for c in range(1, m + 1):
#         if is_safe(node, c, graph, colors):
#             colors[node] = c
#             if backtrack(graph, m, colors, node + 1): return True
#             colors[node] = 0
#     return False

# def get_mrv_node(graph, colors, m):
#     min_options, node = float('inf'), -1
#     for i in range(len(graph)):
#         if colors[i] == 0:
#             opts = sum(1 for c in range(1, m+1) if is_safe(i, c, graph, colors))
#             if opts < min_options:
#                 min_options, node = opts, i
#     return node

# def branch_and_bound(graph, m, colors):
#     if 0 not in colors: return True
#     node = get_mrv_node(graph, colors, m)
#     for c in range(1, m + 1):
#         if is_safe(node, c, graph, colors):
#             colors[node] = c
#             if branch_and_bound(graph, m, colors): return True
#             colors[node] = 0
#     return False

# n = int(input("Nodes: "))
# m = int(input("Colors: "))
# print("Adjacency matrix:")
# graph = [list(map(int, input().split())) for _ in range(n)]

# colors_bt = [0]*n
# print("\nBacktracking:", backtrack(graph, m, colors_bt) and colors_bt or "No solution")

# colors_bb = [0]*n
# print("Branch & Bound:", branch_and_bound(graph, m, colors_bb) and colors_bb or "No solution")
