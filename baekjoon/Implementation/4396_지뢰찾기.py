n = int(input())
array=[list(map(str,input())) for i in range(n)]
open_array = [list(map(str,input())) for i in range(n)]


def open(x,y) :
	dx = [-1,1,0,0,-1,1,1,-1]
	dy = [0,0,-1,1,-1,1,-1,1]

	if open_array[x][y] == 'x':
		ohmygod = 0
		for i in range(8):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == '*':
				ohmygod += 1
		if array[x][y] == '.':
			return ohmygod
		else :
			return -1
	elif open_array[x][y] == '.' :
		return -2

check = 0
temp_list = []
for i in range(n) :
	for j in range(n) :
		temp=open(i,j)
		if temp == -1 :
			check = 1
			break
		elif temp == -2 :
			temp_list.append('.')
		else :
			temp_list.append(str(temp))
	if check==1 :
		break


if check==1 :
	for i in range(n) :
		temp_ = str(''.join(array[i]))
		print(temp_)
else :
	for i in range(n) :
		li = temp_list[n*i:n*i+n]
		temp_ = ''.join(li)
		print(temp_)
