#bfs
import sys
from collections import deque

point = int(sys.stdin.readline())
n, m = map(int, sys.stdin.readline().split())
edge = int(sys.stdin.readline())

array_= [[] for i in range(point+1)]
visited = [False] * (point+1)

for i in range(edge) :
	a, b = map(int,sys.stdin.readline().split())
	array_[a].append(b)
	array_[b].append(a)

q = deque()
q.append((m,0))

check = 0

while q :
	this,count = q.popleft()
	visited[this] = True
	if this==n :
		check = 1
		print(count)
		break
	for i in array_[this] :
		if visited[i] == False :
			q.append((i,count+1))

if check == 0 :
	print(-1)




