case = int(input())
count_list = []
path = []

def dfs(x, y) :
	if x<0 or y<0 or x>=row or y>=col :
		return False
	elif ([x,y] in path) and (visited[path.index([x,y])]==0) :
		visited[path.index([x,y])] = 1
		dfs(x-1,y)
		dfs(x+1,y)
		dfs(x,y+1)
		dfs(x,y-1)
		return True
	elif  ([x,y] not in path) :
		return False

for i in range(case) :
	path = []
	row, col, num = map(int, input().split())
	path = [list(map(int, input().split())) for _ in range(num)]

	visited = [0]*num
	count = 0

	for j in range(len(path)) :
		if dfs(path[j][0], path[j][1])  :
			count+=1

	count_list.append(count)

for i in range(case) :
	print(count_list[i])




