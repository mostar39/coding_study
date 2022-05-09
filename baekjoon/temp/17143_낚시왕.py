import sys

row, col, num = map(int, sys.stdin.readline().split())

array = [[-1]*(col+1) for i in range(row+1)]

information=[]

dict_ = {1:[-1,0], 2:[1,0], 3:[0, 1], 4:[0,-1]}
dire = {1:2, 2:1, 3:4, 4:3}

for i in range(num) :
	r, c, s, d, z = map(int, sys.stdin.readline().split())
	information.append([r,c,s,d,z])


total = 0
for i in range(col) :
	check = 0
	index_ = []
	information.sort(key=lambda x: x[0])
	for j in range(len(information)) :
		r, c, s, d, z = information[j]
		if ((i+1) == c) and (check==0) :
			total += z
			check = 1
			index_.append(j)
		else :
			move_x = abs(dict_[d][0] * s)
			move_y = abs(dict_[d][1] * s)
			change_x = 0
			change_y = 0

			while move_x >= (row - 1) :
				move_x -= (row-1)
				change_x += 1
			if change_x % 2 == 0 :
				information[j][0] = r + dict_[d][0]*(move_x)
			else :
				d = dire[d]
				information[j][3] = d
				information[j][0] = r + dict_[d][0]*(move_x)

			while move_y >= (col - 1) :
				move_y -= (col-1)
				change_y += 1
			if change_y % 2 == 0 :
				information[j][1] = c + dict_[d][1]*(move_y)
			else :
				d = dire[d]
				information[j][3] = d
				information[j][1] = c + dict_[d][1]*(move_y)

		if 	array[information[j][0]][information[j][1]] == -1 :
			array[information[j][0]][information[j][1]] = j
		else :
			in_ = array[information[j][0]][information[j][1]]
			if information[in_][4] < information[j][4] :
				index_.append(in_)
				array[information[j][0]][information[j][1]] = j
			else :
				index_.append(j)

	array = [[-1] * (col + 1) for i in range(row + 1)]

	for k in range(len(index_)) :
		del information[index_[k]]

print(total)



