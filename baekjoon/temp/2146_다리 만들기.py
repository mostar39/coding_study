from collections import deque

n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 1 섬 번호 나누기
def island_num(x,y) :
	global count

	q = deque()
	q.append([x,y])
	visited[x][y] = True
	array[x][y] = count
	while q :
		x,y = q.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and array[nx][ny] == 1 :
				q.append([nx,ny])
				array[nx][ny] = count
				visited[nx][ny] = True

def shortest(num) :
	# 여기에 넣을 때, 0이 아닌 애만 넣어야 함
	global answer
	q = deque()
	dist = [[-1] * n for _ in range(n)]

	for i in range(n):
		for j in range(n) :
			if array[i][j] == num :
				q.append([i,j])
				dist[i][j] = 0
	print('================')
	while q:
		x, y = q.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if (array[nx][ny] == 0) and (dist[nx][ny] == -1):
					dist[nx][ny] = dist[x][y] + 1
					q.append([nx,ny])
				elif (array[nx][ny] > 0) and (array[nx][ny] != num) :
					answer = min(answer, dist[x][y])
					print(dist[x][y])
					print(answer)
					print('Hi')
					return

# 1 섬 번호로 나누기
count = 1
for i in range(n) :
	for j in range(n) :
		if (visited[i][j] == False) and (array[i][j] == 1) :
			island_num(i,j)
			count += 1


# 2 최단거리 도출하기
answer = 100000000
for i in range(1,count) :
	shortest(i)

print(answer)