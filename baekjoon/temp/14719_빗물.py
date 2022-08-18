h,w = map(int,input().split())
list_ = list(map(int,input().split()))
array_ = [[0]*h for _ in range(w)]

for i in range(len(list_)) :
	array_[i][:list_[i]] = [1] * list_[i]

visited = [[0]*h for _ in range(w)]

#sign = 0 => 위쪽 체크
#sign = 1 => 아래쪽 체크
def find_1(i,j,sign) :
	global top_x, top_y
	global bottom_x, bottom_y

	visited[i][j] = 1

	if sign == 0 :
		nx = i - 1
		ny = j
	elif sign==1 :
		nx = i + 1
		ny = j

	if 0<=nx<w and 0<=ny<h :
		if array_[nx][ny] == 1 :
			if sign == 0 :
				top_x = nx
				top_y = ny
			else :
				bottom_x = nx
				bottom_y = ny
		elif array_[nx][ny] == 0 and visited[nx][ny] == 0:
			find_1(nx,ny,sign)

count = 0
for i in range(w) :
	for j in range(h) :
		if array_[i][j] == 0 and visited[i][j] == 0 :
			top_x, top_y = -1, -1
			find_1(i,j,0)
			bottom_x, bottom_y = -1, -1
			find_1(i,j,1)
			if top_x != -1 and bottom_x != -1 :
				count += (bottom_x - top_x - 1)
				# print(count)

print(count)


h,w = map(int,input().split())
list_ = list(map(int,input().split()))
answer = 0

for i in range(1,w-1) :
	pre_ = max(list_[:i])
	next_ = max(list_[i+1:])
	hi = min(pre_,next_)
	if list_[i] < hi :
		answer += hi - list_[i]
print(answer)