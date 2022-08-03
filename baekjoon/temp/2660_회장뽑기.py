n = int(input())
temp = [0,0]
dict_ = {}

for i in range(1,n+1) :
	dict_[i] = []

while True :
	try:
		temp =list(map(int,input().split()))
		dict_[temp[0]].append(temp[1])
		dict_[temp[1]].append(temp[0])
	except :
		break


def dfs(visited,what,time) :
	for hey in dict_[what] :
		if (visited[hey] == 0) or (time<visited[hey]) :
			visited[hey] = time+1
			dfs(visited,hey,time+1)

answer = []
small = n+1

for i in range(1,n+1) :
	visited=[0]* (n+1)
	visited[i]=-1
	dfs(visited,i,0)
	score = max(visited)
	if score < small :
		small = score
	answer.append(max(visited))

print(small, answer.count(small))

for i in range(len(answer)) :
	if answer[i] == small :
		print((i+1), end=' ')