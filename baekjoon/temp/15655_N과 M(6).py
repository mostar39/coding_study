n, m = map(int,input().split())
list_ = list(map(int,input().split()))
list_.sort()

answer= []

def dfs(depth) :
	if len(answer) == m :
		print(*answer)
	else :
		for i in range(depth,len(list_)) :
			answer.append(list_[i])
			dfs(i+1)
			answer.pop()
dfs(0)
