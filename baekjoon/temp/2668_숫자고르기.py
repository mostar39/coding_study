n = int(input())
dict_ = {}
for i in range(n) :
	dict_[i+1] = int(input())

def dfs(now) :
	if visited[now] == 1 :
		return
	else :
		head.append(now)
		tail.append(dict_[now])
		visited[now] = 1
		dfs(dict_[now])

answer = []
answer_temp = []
temp = []

for i in range(1,n+1) :
	head = []
	tail = []
	visited = [0] * (n+1)
	dfs(i)
	if (set(head) == set(tail)) and (len(set(head) & set(answer)) == 0):
		answer += head
	elif (set(head) == set(tail)) and len(answer) < len(head) :
		answer = list(head)
	elif (set(head) == set(tail)) and len(head) == 1 :
		temp.append(head[0])


answer = list(set(answer + temp))
answer.sort()
print(len(answer))
for i in range(len(answer)) :
	print(answer[i])