import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

for k in range(n) :
	for a in range(n) :
		for b in range(n) :
			if graph[a][k]==1 and graph[k][b]==1 :
				graph[a][b] = 1


for a in range(n) :
	for b in range(n) :
		print(graph[a][b], end = ' ')
	print()