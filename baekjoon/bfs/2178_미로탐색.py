import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
array = [(list(map(int,input()))) for i in range(n)]

queue = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue.append([0,0])
result = 0

while queue :
	x,y = queue.popleft()
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<m :
			if array[nx][ny] == 1 :
				array[nx][ny] = array[x][y] + 1
				queue.append([nx,ny])

print(array[n-1][m-1])
