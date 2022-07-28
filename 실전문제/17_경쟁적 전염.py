# 시간초과

n, k = map(int,input().split())

array = [list(map(int,input().split())) for i in range(n)]
s, q_x, q_y = map(int,input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

check = [[] for _ in range(k+1)]

def dfs(x,y,num) :
	check[num].remove([x,y])
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n :
			if array[nx][ny] == 0 :
				array[nx][ny] = num
				check[num].append([nx,ny])

for i in range(n) :
	for j in range(n) :
		if array[i][j] != 0 :
			check[array[i][j]].append([i,j])

for _ in range(s):
	for i in range(1,k+1) :
		temp = list(check[i])
		for p,q in temp :
			dfs(p,q,i)

print(array[q_x-1][q_y-1])