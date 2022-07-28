from collections import deque

# 0,0 -> m-1,n-1
n, m = map(int,input().split())
array = [list(map(int,input())) for i in range(m)]
visited = [[-1] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


q = deque()
q.append([0,0])
visited[0][0] = 0

while q :
	x, y = q.popleft()
	if x==m-1 and y==n-1 :
		break
	for i in range(len(dx)) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<m and 0<=ny<n:
			if visited[nx][ny] == -1 :
				if array[nx][ny] == 0 :
					q.appendleft([nx,ny])
					visited[nx][ny] = visited[x][y]
				elif array[nx][ny] == 1 :
					q.append([nx,ny])
					visited[nx][ny] = visited[x][y]+1

print(visited[m-1][n-1])
