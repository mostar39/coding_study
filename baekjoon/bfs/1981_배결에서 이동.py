import sys
from collections import deque

n = int(sys.stdin.readline())
array = [sys.stdin.readline() for i in range(n)]

# 증가하는 쪽으로만 가야함
# 하나하나 다 봐야하나 ?
dx = [1,0]
dy = [0,1]

temp_array =[[999999999]*n for _ in range(n)]

def bfs(x,y) :
	q = deque()
	q.append([x,y,201])

	while q :
		i, j, is_max = q.popleft()
		for k in range(2) :
			nx = i + dx[k]
			ny = j + dy[k]
			if 0<=nx<n and 0<=ny<n and temp_array[nx][ny] >= max(is_max,array[nx][ny]) - min(is_min, array[nx][ny]) :
				is_max = array[nx][ny]
				q.append([nx,ny,is_max])
				temp_array[nx][ny] = max(is_max,array[nx][ny]) - min(is_min, array[nx][ny])


bfs(0,0)
print(temp_array[n-1][n-1])


