import heapq
import sys

INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
	a, b, c = map(int, sys.stdin.readline().split())
	graph[a].append((b,c))

def dijkstra(start) :
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0
	while q :
		dist, now = heapq.heappop(q)
		# 이미 더 짧은 거 잘 잡고 있음
		if distance[now] < dist :
			continue
		# 현재 노드와 연결된 다른 인접한 노드 확인
		for i in graph[now] :
			cost = dist + i[1]
			if cost < distance[i[0]] :
				distance[i[0]] = cost
				heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1, n+1) :
	if distance[i] == INF :
		print('INFINITY')
	else :
		print(distance[i])