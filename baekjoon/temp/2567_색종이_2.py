n = int(input())

array= [[0]*102 for i in range(102)]
count_array = [[0]*102 for i in range(102)]

for i in range(n) :
	x, y = map(int,input().split())
	for p in range(10) :
		for q in range(10) :
			array[x+p][y+q] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

real_count = 0
for p in range(1,101) :
	for q in range(1,101) :
		count_num = 0
		if array[p][q] == 1 :
			continue
		for i in range(4) :
			new_x = p + dx[i]
			new_y = q + dy[i]
			if (array[new_x][new_y] == 1):
				real_count += 1
print(real_count)

result = 0
for p in range(1,101) :
	for q in range(1, 101) :
		if array[p][q] == 1 :
			count = 0
			for i in range(4) :
				new_x = p + dx[i]
				new_y = q + dy[i]
				if array[new_x][new_y] == 1:
					count+=1
			if count == 2 :
				result += 2
			if count == 3 :
				result += 1

print(result)

