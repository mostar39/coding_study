n = int(input())
array = [[0]*102 for i in range(102)]
for i in range(n) :
	start_x, start_y = map(int,input().split())
	for p in range(10) :
		for q in range(10) :
			array[start_x+p][start_y+q] = 1

direction = [[0,1],[1,0]]
max_value = 100
#가로 입장에서 봐주고 세로입장에서 봐줘야 하나?
for i in range(1,102) :
	for j in range(1,102) :
		if array[i][j] == 1 :
			row_count = 1
			for p in range(i+1,102) :
				if array[p][j] == 1 :
					row_count += 1
				else:
					break
			row_col_count = 0
			temp = list(array[i:i+row_count])
			for t in range(j, 102) :
				if sum(list(zip(*temp))[t]) == row_count :
					row_col_count += 1
				else:
					break
			max_value = max(max_value, row_count * row_col_count)

			col_count = 1
			for q in range(j+1,102) :
				if array[i][q] == 1 :
					col_count += 1
				else :
					break

			temp = list(zip(*array))[j:j+col_count]

			col_row_count = 0
			for t in range(i, 102) :
				if sum(list(zip(*temp))[t]) == col_count :
					col_row_count += 1
				else:
					break


			max_value = max(max_value, col_count * col_row_count)


print(max_value)
