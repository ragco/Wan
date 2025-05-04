import heapq

def a_star_search(start, goal, graph, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  # (f, g, current, path)
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (g + cost + heuristic[neighbor], g + cost, neighbor, path + [neighbor]))

    print("Path does not exist!")
    return None

# Example graph and heuristic (Romania map style)
graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}
# User input
start = input("Enter the start node: ").strip().upper()
goal = input("Enter the goal node: ").strip().upper()
# Run
a_star_search('A', 'G', graph, heuristic)
