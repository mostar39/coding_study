import sys
sys.setrecursionlimit(10**9)

n, m = map(int,sys.stdin.readline().split())
connect = [[] for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m) :
	temp = list(map(int,sys.stdin.readline().split()))
	temp.sort()
	connect[temp[0]].append(temp[1])
	connect[temp[1]].append(temp[0])

def dfs(num) :
	if (visited[num] == False) :
		visited[num] = True
		for k in connect[num]:
			dfs(k)
		return True
	else :
		return False

count = 0
for i in range(1,n+1) :
	if dfs(i) :
		count += 1

print(count)