import sys
from collections import deque

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
start = int(sys.stdin.readline())
visited = [False] * len(array)

q = deque()
q.append(start)

while q :
	now = q.popleft()
	if visited[now-1] == False :
		visited[now-1] = True
		jump=array[now-1]
		dx = [jump,-jump]
		for i in range(2) :
			nx = now + dx[i]
			if 1<=nx<=n :
				q.append(nx)

count = 0
for i in range(len(visited)) :
	if visited[i] :
		count += 1

print(count)