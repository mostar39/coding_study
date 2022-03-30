import sys
sys.setrecursionlimit(10**6)
n, m = map(int,sys.stdin.readline().split())
array = [list(map(str,input())) for i in range(n)]

def dfs(x,y,what) :
	if x<=-1 or y<=-1 or x>=n or y>=m :
		return False
	if (array[x][y] == '-') and (what=='-') :
		array[x][y] = '0'
		dfs(x, y+1,'-')
		dfs(x, y-1,'-')
		return True
	if (array[x][y] == '|') and (what=='|') :
		array[x][y] = '0'
		dfs(x+1, y, '|')
		dfs(x-1, y,'|')
		return True
	return False

count = 0

for i in range(n) :
	for j in range(m) :
		if dfs(i,j,array[i][j]) :
			count+=1


print(count)