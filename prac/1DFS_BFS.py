from collections import deque

def dfs_recursive(node, visited, graph):
    """Recursive DFS traversal"""
    if node not in visited:  # If the node hasn't been visited
        print(node, end=' ')  # Print the current node
        visited.add(node)  # Mark the node as visited
        for neighbor in graph.get(node, []):  # Visit all neighbors of the current node
            dfs_recursive(neighbor, visited, graph)  # Recursively call DFS for each neighbor

def bfs_recursive(queue, visited, graph):
    """Recursive BFS traversal"""
    if not queue:  # If the queue is empty, stop the recursion
        return
    node = queue.popleft()  # Dequeue the first element
    if node not in visited:  # If the node hasn't been visited
        print(node, end=' ')  # Print the current node
        visited.add(node)  # Mark the node as visited
        for neighbor in graph.get(node, []):  # Visit all neighbors of the current node
            if neighbor not in visited:  # Only add unvisited neighbors to the queue
                queue.append(neighbor)
    bfs_recursive(queue, visited, graph)  # Recursively call BFS for the next nodes in the queue

# --------- INPUT GRAPH ----------
graph = {}  # Initialize an empty graph dictionary
num_edges = int(input("Enter number of edges: "))  # Ask user for the number of edges
for _ in range(num_edges):  # Loop over each edge
    u, v = map(int, input("Enter edge (u v): ").split())  # Read an edge (u, v)
    graph.setdefault(u, []).append(v)  # Add v to the adjacency list of u
    graph.setdefault(v, []).append(u)  # Add u to the adjacency list of v (undirected graph)

start = int(input("Enter starting node: "))  # Ask user for the starting node

# --------- USER CHOICE ----------
choice = input("Choose traversal (DFS/BFS): ").strip().lower()  # Ask user for DFS or BFS choice

print("\nTraversal Output:", end=' ')  # Display the traversal output message
if choice == 'dfs':  # If user chose DFS
    visited = set()  # Create an empty set to keep track of visited nodes
    dfs_recursive(start, visited, graph)  # Start DFS traversal from the 'start' node
elif choice == 'bfs':  # If user chose BFS
    visited = set()  # Create an empty set to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    bfs_recursive(queue, visited, graph)  # Start BFS traversal using recursion
else:  # If user entered an invalid choice
    print("Invalid choice. Please enter 'DFS' or 'BFS'.")  # Inform the user abo
