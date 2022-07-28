from collections import deque
#(1,1) -> (n,m)까지 이동
# 이동 오른쪽 and 위 --> (1,0), (0,1)
n, m, item_num, error_num = map(int,input().split())
array = [[0]*(m+1) for i in range(n+1)]

item_position = []
for i in range(item_num) :
	te_x, te_y = map(int,input().split())
	array[te_x][te_y] = 1
	item_position.append([te_x,te_y])

item_position.sort(key = lambda x:[])


for i in range(error_num) :
	te_x, te_y = map(int,input().split())
	array[te_x][te_y] = 2

move_x = [0, 1]
move_y = [1, 0]

count = 0
q = deque()
q.append([1,1,item_position[0][0],item_position[0][1]])
target_index = 0
max_len = -1

while q :
	x,y,item_x_target, item_y_target=q.popleft()
	for i in range(2) :
		nx = x + move_x[i]
		ny = y + move_y[i]
		if (1<=nx<=n) and (1<=ny<=m) :
			if array[nx][ny] == 0 :
				q.append([nx,ny,item_x_target, item_y_target])
			elif array[nx][ny] == 1 :
				q.append([nx,ny,item_x_target, item_y_target])
			if (nx == item_x_target) and (ny == item_y_target):
				count+=1
				q = deque()
				if target_index+1 < item_num :
					q.append([item_position[target_index][0], item_position[target_index][1], item_position[target_index+1][0],item_position[target_index+1][1]] )
				target_index += 1

print(count)

