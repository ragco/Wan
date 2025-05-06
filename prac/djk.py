import heapq

def djkstra(graph , start):
    pq = [(0, start)]
    dist = {vrtx : float('inf') for vrtx in graph}
    dist[start] = 0

    while pq:
        cur_dist , cur_vrtx = heapq.heappop(pq)

        if cur_dist > dist[cur_vrtx]:
            continue

        for ngbr , wt in graph[cur_vrtx]:
            distnc = cur_dist + wt
            if distnc < dist[ngbr]:
                dist[ngbr] = distnc
                heapq.heappush(pq , (distnc , ngbr))
    return dist

n = int(input("Enterr number of nodes : " ))
print ( "enter node names : ")
nodenames = [input(f"node {i+1} : ") for i in range (n)]

graph = {}
for node in nodenames:
    graph[node] = []

nedge = int(input("Enter no of Edges : "))
print("Enter Edgs in ST END WT")

for i in range(nedge):
    u , v , w = input.split()
    w = int(w)
    graph[u].append((v,w))
    graph[v].append((u,w))

strt = input("Enter starting node : ")
djk = djkstra(graph , strt)
print("\nShortest distance from ", strt)
for node in nodenames:
    print(f"{strt} -> {node} = {djk[node]}")
    