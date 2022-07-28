from collections import deque
import sys

sys.setrecursionlimit(10**9)

n = int(input())
array = [[] for i in range(n+1)]

for _ in range(n-1) :
	start, end, path = map(int,input().split())
	array[start].append([end,path])
	array[end].append([start,path])

distance = [-1] * (n+1)
distance[1] = 0

def dfs(x,wei) :
	for i in array[x] :
		a,b = i
		if distance[a] == -1 :
			distance[a] = wei + b
			dfs(a, wei+b)

dfs(1,0)

new_start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[new_start] = 0
dfs(new_start,0)

print(max(distance))
