import sys, heapq

n, e = map(int, sys.stdin.readline().split())

INF = 2147483647
dist = [INF for _ in range(n+1)]
dist[1] = 0

adj_list = [[] for _ in range(n+1)]

for _ in range(e) :
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append((1, b))  # (가중치, 노드)
    adj_list[b].append((1, a))

hq = []
for w, v in adj_list[1] :
    heapq.heappush(hq, (w, v))

def dijkstra(hq) :
    while hq :
        # 가장 낮은 거리를 가진 거리와 노드 추출
        distance, node = heapq.heappop(hq)

        if dist[node] > distance :
            dist[node] = distance

            for w, v in adj_list[node] :
                heapq.heappush(hq, (w + distance, v))

dijkstra(hq)

print(dist.index(max(dist[1:])), max(dist[1:]), dist.count(max(dist[1:])))