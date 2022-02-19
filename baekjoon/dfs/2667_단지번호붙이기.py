n = int(input())
path = []

for i in range(n) :
	temp = list(map(int, input()))
	path.append(temp)


def dfs(x,y) :
	if x<0 or y<0 or x>=n or y>=n:
		return False
	if (path[x][y] == 1) :
		global house_count
		house_count += 1
		path[x][y]=0
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y+1)
		dfs(x, y-1)
		return True
	return False

count = 0
house_count = 0
count_house = []
for i in range(n) :
	for j in range(n) :
		if dfs(i,j) == True:
			count_house.append(house_count)
			count += 1
			house_count = 0

count_house.sort()
print(count)
for i in range(len(count_house)) :
	print(count_house[i])


