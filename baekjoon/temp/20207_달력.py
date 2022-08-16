n = int(input())
array = []

max_ = -1
for i in range(n) :
	start, end = map(int,input().split())
	array.append([start,end,(end-start+1)])
	if max_ < end :
		max_ = end

visited = [[0] * max_ for i in range(n)]
# real_visited = [[0] * max_ for i in range(n)]
array.sort(key=lambda x:(x[0], (-x[2])))

for i in range(len(array)) :
	k = 0
	start, end, during = array[i]
	while True :
		if sum(visited[k][start-1:end]) == 0 :
			visited[k][start-1:end] = [1] * during
			break
		else :
			k += 1

hi = list(zip(*visited))
answer = 0
count = 0
max_col = -1
for i in range(len(hi)) :
	col = sum(list(hi[i]))
	if col == 0 :
		answer += count*max_col
		count = 0
		max_col = -1
	else :
		max_col = max(max_col,col)
		count += 1
	if i == len(hi)-1 :
		answer += count * max_col
print(answer)

# dx = [1,0]
# dy = [0,1]
# def dfs(x,y) :
# 	global min_y
# 	global max_y
# 	global max_x
#
# 	real_visited[x][y] = 1
# 	min_y = min(min_y,y)
# 	max_y = max(max_y,y)
# 	max_x = max(max_x,x)
#
# 	for i in range(len(dx)) :
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if 0<=nx<n and 0<ny<max_ :
# 			if visited[nx][ny] == 1 :
# 				dfs(nx,ny)
#
# answer = 0
# for i in range(len(visited)) :
# 	for j in range(len(visited[0])) :
# 		min_y = max_
# 		max_y = -1
# 		max_x = -1
# 		if visited[i][j] == 1 and real_visited[i][j] == 0 :
# 			dfs(i,j)
# 			answer += (max_x + 1) * (max_y-min_y+1)
#
#
# print(answer)