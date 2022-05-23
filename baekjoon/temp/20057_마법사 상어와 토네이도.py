n = int(input())
array = [list(map(int,input().split())) for i in range(n)]

left = [[-1, 1, 0.01], [1,1,0.01], [-2,0,0.02], [2, 0, 0.02], [0, -2, 0.05], [-1, 0, 0.07], [1, 0, 0.07],
		[-1, -1, 0.1], [1, -1, 0.1], [0, -1, -1]]
right = [[i, -j, k] for i, j, k in left]
up = [[j, i, k] for i, j, k in left]
down = [[-j,i,k] for i, j, k in left]

new_x, new_y = n//2, n//2

# 0 : 좌, 1 : 아래, 2 : 우, 3: 위
direction = 0 # index
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]

root = 1
answer = 0
signal = 0

while True :
	if signal == 1 :
		break
	if root == n :
		signal = 1
		root = n-1
	temp_root = int(root)
	temp_direction = int(direction)

	if temp_direction == 0:
		what = list(left)
		direction += 1
	elif temp_direction == 1:
		what = list(down)
		root += 1
		direction += 1
	elif temp_direction == 2:
		what = list(right)
		direction += 1
	else:
		what = list(up)
		root += 1
		direction =0

	for i in range(temp_root) :
		new_x = new_x + move[temp_direction][0]
		new_y = new_y + move[temp_direction][1]
		sand = array[new_x][new_y]
		array[new_x][new_y] = 0
		how_many = 0
		for move_x, move_y, power in what :
			temp_x = new_x + move_x
			temp_y = new_y + move_y
			# 밖으로 나가
			if (temp_x<0) or (temp_x>=n) or (temp_y<0) or (temp_y>=n) :
				if power == -1 :
					# 지금까지 이동했던 거 뺀 거
					answer += (sand-how_many)
				else :
					# 정답에만 어느정도 넘쳤는지 더해주고
					answer += int(sand * power)
					how_many += int(sand * power)
			# 밖으로 안나가
			else :
				if power == -1:
					array[temp_x][temp_y] += (sand - how_many)
				else :
					wow = int(sand * power)
					array[temp_x][temp_y] += wow
					how_many += int(wow)

print(answer)


