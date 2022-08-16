n = int(input())
array = [[0]*n for i in range(n)]
student = []
student_pos = {}
student_like = {}

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_null_arr(x,y) :
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	count = 0
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n and array[nx][ny] == 0 :
			count += 1
	return count

def find_friend_arr(x,y,like_list) :
	count = 0
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n and (array[nx][ny] in like_list) :
			count += 1
	return count

def find_fun(like) :
	max_null_where =[n,n]
	max_null = -1
	max_real_null = -1
	for i in range(n) :
		for j in range(n) :
			if array[i][j] != 0 :
				continue
			if len(like) == 0 :
				num = find_null_arr(i, j)
				if num > max_null:
					max_null_where = [n, n]
					max_null = num
				if num >= max_null :
					if i < max_null_where[0]:
						max_null_where[0] = i
						max_null_where[1] = j
					elif (i == max_null_where[0]) and (j < max_null_where[1]):
						max_null_where[0] = i
						max_null_where[1] = j
			else :
				num = find_friend_arr(i, j, like)
				null_num = find_null_arr(i,j)
				if num > max_null:
					max_null_where = [n, n]
					max_null = num
					max_real_null = -1

				if num >= max_null :
					if null_num > max_real_null :
						max_real_null = null_num
						max_null_where[0] = i
						max_null_where[1] = j
					elif null_num == max_real_null :
						if i < max_null_where[0]:
							max_null_where[0] = i
							max_null_where[1] = j
						elif (i == max_null_where[0]) and (j < max_null_where[1]):
							max_null_where[0] = i
							max_null_where[1] = j

	return max_null_where


def find_arr(student_num, like_people) :
	student.append(student_num)
	if len(set(like_people) & set(student)) == 0 :
		x,y = find_fun([])
	else :
		x, y =find_fun(like_people)
	array[x][y] = student_num
	student_pos[student_num] = [x,y]



for i in range(n*n) :
	temp = list(map(int,input().split()))
	find_arr(temp[0],temp[1:])
	student_like[temp[0]] = temp[1:]

total_score = 0
for i in range(1,n*n+1) :
	x,y = student_pos[i]
	score = find_friend_arr(x,y,student_like[i])
	if score==0 :
		score += 0
	else :
		total_score += 10**(score-1)

print(total_score)
