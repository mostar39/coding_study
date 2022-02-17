from collections import deque

n,m = map(int,input().split())

path = []

for i in range(n) :
	path.append(list(map(int,input())))

queue = deque()

def bfs(x,y) :
	#상 하 좌 우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	queue.append((x,y))

	while queue :
		x,y = queue.popleft()
		for i in range(4) :
			nx = x + dx
			ny = y + dy

			if nx<0 or ny<0 or nx>=n or ny>=m :
				continue
			if path[nx][ny] == 0 :
				continue
			if path[nx][ny] == 1 :
				queue.append((nx,ny))
				path[nx][ny] = path[x][y] + 1

	return path[n-1][m-1]

print(bfs(0,0))