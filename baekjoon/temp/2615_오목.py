import sys

array = [list(map(int,input().split())) for i in range(19)]
visited = [[0]*19 for _ in range(19)]

dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]

def dfs(x,y,what,direction,count) :
	global sign

	nx = x + dx[direction]
	ny = y + dy[direction]

	if 0<=nx<19 and 0<=ny<19 :
		if count == 5 and (array[nx][ny] != what):
			sign = 1
			return
		if (array[nx][ny] == what)  :
			dfs(nx,ny,what,direction, count+1)
	else :
		if count == 5 :
			sign=1
			return

for i in range(19) :
	for j in range(19) :
		if (array[i][j] != 0):
			for k in range(len(dx)) :
				sign = 0
				dfs(i,j,array[i][j],k,1)
				if (sign == 1) :
					if 0<=(i - dx[k])<19 and 0<=(j - dy[k])<19 :
						if array[i - dx[k]][j - dy[k]] != array[i][j] :
							print(array[i][j])
							print(i+1, j+1)
							sys.exit()
					else :
						print(array[i][j])
						print(i + 1, j + 1)
						sys.exit()

print(0)