import heapq

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
src, dst = map(int, input().split())

dist = {i: float("inf") for i in range(n)}
dist[src] = 0
parent = {src: None}
pq = [(0, src)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v in range(n):
        w = matrix[u][v]
        if w > 0 and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            heapq.heappush(pq, (dist[v], v))

path, curr = [], dst
while curr is not None:
    path.append(curr)
    curr = parent.get(curr)
path.reverse()

print(f"Shortest Distance: {dist[dst]}")
print(f"Shortest Path: {' -> '.join(map(str, path))}")
