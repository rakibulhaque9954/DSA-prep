import heapq

# Function to calculate the distance between two cities considering the grid's wrap-around nature
def distance(x1, y1, x2, y2, H, W):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    dx = min(dx, W - dx)
    dy = min(dy, H - dy)
    return dx + dy

# Function to build a complete graph with cities as nodes and distances as edge weights
def build_complete_graph(N, coordinates, H, W):
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        for j in range(i + 1, N):
            dist = distance(*coordinates[i], *coordinates[j], H, W)
            graph[i].append((j, dist))
            graph[j].append((i, dist))
    
    return graph

# Function to find the Minimum Spanning Tree (MST) of the complete graph
def find_mst(graph):
    visited = [False] * len(graph)
    min_heap = [(0, 0)]  # (weight, node)
    mst_weight = 0
    
    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        mst_weight += weight
        for neighbor, neighbor_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (neighbor_weight, neighbor))
    
    return mst_weight

# Input
N, H, W = map(int, input().split())
coordinates = [list(map(int, input().split())) for _ in range(N)]

    # # Build a complete graph
    # graph = build_complete_graph(N, coordinates, H, W)


graph = build_complete_graph(N2, cities2, H2, W2)
mst_weight = find_mst(graph)
# Output the minimum total distance
print(mst_weight)
