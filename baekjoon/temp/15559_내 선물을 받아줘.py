import sys

row,col = map(int,sys.stdin.readline().split())
array = [list(map(str,sys.stdin.readline().strip())) for i in range(row)]
array_copy = [[0] * col for i in range(row)]

def dfs(x,y,cnt) :
	dict_ = {'N':[-1,0],'S':[1,0],'W':[0,-1],'E':[0,1]}
	if x<0 or x>=row or y<0 or y>=col :
		return False
	if array_copy[x][y] :
		return array_copy[x][y]
	temp_x = x + dict_[array[x][y]][0]
	temp_y = y + dict_[array[x][y]][1]
	array_copy[x][y] = cnt
	array_copy[x][y] =dfs(temp_x,temp_y, cnt)
	return array_copy[x][y]

count=0
for i in range(row) :
	for j in range(col) :
		if not array_copy[i][j] :
			a = dfs(i,j,count+1)
			count = max(a,count)

print(count)
#===================================

n, m = map(int, input().split())
MAP = [list(input()) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dic = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}


def dfs(y, x, cnt):
	global n, m

	if check[y][x]:
		return check[y][x]

	check[y][x] = cnt
	print(cnt)
	ny = y + dic[MAP[y][x]][0]
	nx = x + dic[MAP[y][x]][1]
	check[y][x] = dfs(ny, nx, cnt)
	return check[y][x]


result = 0
for i in range(n):
	for j in range(m):
		if not check[i][j]:
			a = dfs(i, j, result + 1)
			result = max(a, result)

print(result)