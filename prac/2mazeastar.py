import heapq 
#heapq is a module in Python that allows you to maintain a priority queue (where the smallest element is always easily accessible)

def astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_list = [] #Create a priority queue to store nodes to explore
    heapq.heappush(open_list, (0, start)) #(0, start) is a tuple has the form (f_score, (row, col))
    #The heap stores the start node with a priority (f_score) of 0 because it’s the first #node to explore
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list) #_ is a placeholder for values we don’t need
        # we only care about the current position (node) to explore next, so we don’t need #the f_score for further computations after we’ve popped the node.
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] #(backtracking from goal to start), this reverses the path #list to get the correct order (start to goal)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != 1:
                temp_g = g_score[current] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score = temp_g + abs(neighbor[0]-end[0]) + abs(neighbor[1]-end[1])
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current
    return None

def print_maze(maze, path): #maze is 2D matrix & path is list of Tuples
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r,c) in path:
                print('.', end=' ')
            elif maze[r][c] == 1:
                print('X', end=' ')
            else:
                print('-', end=' ')
        print()

# --- TAKE INPUT FROM USER ---

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the maze row by row (0 = empty, 1 = wall):")
maze = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    maze.append(row)

start_x = int(input("Enter start X (row index): "))
start_y = int(input("Enter start Y (col index): "))
end_x = int(input("Enter end X (row index): "))
end_y = int(input("Enter end Y (col index): "))

start = (start_x, start_y)
end = (end_x, end_y)

# --- CALL ASTAR ---
path = astar(maze, start, end)

if path:
    print_maze(maze, path)
    print("Path found!")
else:
    print("No path found.")
