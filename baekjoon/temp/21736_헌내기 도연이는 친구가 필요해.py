import sys
from collections import deque

row, col = map(int,sys.stdin.readline().split())

array = []
for i in range(row) :
	temp =list(map(str,sys.stdin.readline().strip()))
	if 'I' in temp :
		my_position = [i,temp.index('I')]
	array.append(temp)

q = deque()
q.append(my_position)

array[my_position[0]][my_position[1]] = 'X'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

while q :
	x,y = q.pop()
	for i in range(4) :
		temp_x = x+dx[i]
		temp_y = y+dy[i]
		if 0<=temp_x<row and 0<=temp_y<col :
			if array[temp_x][temp_y] == 'O' :
				array[temp_x][temp_y] = 'X'
				q.append([temp_x,temp_y])
			elif array[temp_x][temp_y] == 'P' :
				count += 1
				array[temp_x][temp_y] = 'X'
				q.append([temp_x, temp_y])

if count==0:
	print('TT')
else :
	print(count)

