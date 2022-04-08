import sys

n = int(sys.stdin.readline())
array = []
for i in range(n) :
	array.append(list(map(int,sys.stdin.readline().split())))

check = 0
def dfs(x,y) :

	global check
	if array[x][y] == -1 :
		check +=1
	dx = [0,array[x][y]*1]
	dy = [array[x][y]*1,0]
	for j in range(array[x][y]) :
		for i in range(len(dx)) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (0<=nx<=n-1) and (0<=ny<=n-1) :
				dfs(nx,ny)

dfs(0,0)
if check!=0 :
	print('HaruHaru')
else :
	print('Hing')


