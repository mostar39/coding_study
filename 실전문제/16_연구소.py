n, m = map(int,input().split())

array = []
temp = [[0]*m for i in range(n)]

for i in range(n) :
	array.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

result = 0

#퍼져라 얍 !
def virus(x,y) :
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<m :
			if temp[nx][ny] == 0 :
				temp[nx][ny] = 2
				virus(nx,ny)

def get_score() :
	score = 0
	for i in range(n) :
		for j in range(m) :
			if temp[i][j] == 0 :
				score += 1
	return score

def dfs(count) :
	global result
	if count == 3 :
		for i in range(n) :
			for j in range(m) :
				temp[i][j] = array[i][j]

		for i in range(n) :
			for j in range(m) :
				if temp[i][j] == 2 :
					virus(i,j)
		result = max(result, get_score())
		return

	for i in range(n) :
		for j in range(m) :
			if array[i][j] == 0 :
				array[i][j] = 1
				count += 1
				dfs(count)
				array[i][j] = 0
				count -= 1

dfs(0)
print(result)