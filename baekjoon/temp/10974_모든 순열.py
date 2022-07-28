n = int(input())
visited = [0] * n

def dfs(depth) :
	if depth == n :
		print(*visited)
	else :
		for i in range(n) :
			if i+1 in visited :
				continue
			visited[depth] = i+1
			dfs(depth+1)
			visited[depth] = 0

dfs(0)