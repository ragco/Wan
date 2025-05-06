from collections import deque

graph = {}
num  = int(input("Enter edges num : "))
for _ in range (num):
    u , v = map(int , input("Enter edge from and to : ").split())
    graph.setdefault(u , []).append(v)
    graph.setdefault(v , []).append(u)
start = int(input("Enter Starting graph : "))
visited = set()
queue = deque([start])

def bfs (queue , visited , graph):
    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        print(node , end =" ")
        visited.add(node)
        for ngbr in graph[node]:
            if ngbr not in visited:
                queue.append(ngbr)
    bfs (queue , visited , graph)

def dfs(node , visited , graph):
    if node not in visited:
        print(node , end =" ")
        visited.append(node)
        for  nbr in graph(node):
            dfs(nbr , visited , graph)


bfs (queue , visited , graph)