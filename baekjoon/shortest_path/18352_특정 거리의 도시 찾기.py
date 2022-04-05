import sys
from collections import deque

N, M, K, X = map(int,sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
for i in range(M) :
	start, end= map(int, sys.stdin.readline().split())
	graph[start].append(end)

distance = [-1] * (N+1)
distance[X] = 0
q = deque()
q.append(X)

while q :
	now = q.popleft()
	for i in graph[now] :
		if distance[i] == -1 :
			distance[i] = distance[now] + 1
			q.append(i)

check = 0
for i in range(1, N+1) :
	if distance[i] == K :
		check = 1
		print(i)
	if i==N and check == 0 :
		print(-1)

