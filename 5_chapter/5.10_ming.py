n, m = map(int, input().split())

path = []

for i in range(n) :
	temp_path = list(map(int, input()))
	path.append(temp_path)

def dfs(x,y) :
	if x<=-1 or y<=-1 or x>=n or y>=m :
		return False
	if path[x][y] == 0 :
		path[x][y]=1
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		return True

	return False

count = 0

for i in range(n) :
	for j in range(m) :
		if dfs(i,j) :
			count+=1

print(count)