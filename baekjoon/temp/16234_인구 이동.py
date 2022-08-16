import sys

#sys.setrecursionlimit(10**7)

n, min_, max_ = map(int,input().split())
array = [list(map(int,input().split())) for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[0] * n for i in range(n)]

def dfs(x,y,num) :
	global sum_
	global pos

	visited[x][y] = num
	sum_+=array[x][y]
	pos.append([x,y])

	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if (0<=nx<n) and (0<=ny<n) :
			if (min_ <= abs(array[x][y]-array[nx][ny]) <= max_) and (visited[nx][ny] == 0) :
				dfs(nx,ny,num)

howmany = 0
num = 1
sign = 0
while num!=(n*n)+1 :
	visited = [[0] * n for i in range(n)]
	num = 1
	for i in range(n) :
		for j in range(n) :
			sum_ = 0
			if visited[i][j] == 0 :
				pos = []
				dfs(i,j,num)
				split_ = int(sum_/len(pos))
				for k in pos :
					array[k[0]][k[1]] = split_
	howmany += 1

print(howmany-1)