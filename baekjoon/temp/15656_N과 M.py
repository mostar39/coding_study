n, m = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
visited = []

def dfs(depth) :
	if depth == m :
		for i in range(len(visited)) :
			print(array[visited[i]], end=' ')
		print()
	else :
		for i in range(n) :
			visited.append(i)
			dfs(depth+1)
			visited.pop()

dfs(0)