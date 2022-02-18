from collections import deque

n, m, start = map(int, input().split())

path = []
for i in range(m) :
	path.append(list(map(int, input().split())))

visit_dfs = [False] * (n+1)
visit_bfs = [False] * (n+1)

def dfs(path, i, visit_dfs) :
	visit_dfs[i] = True
	print(i, end=' ')
	path_two = []
	for t in range(m) :
		if path[t][0] == i :
			path_two.append(path[t][1])
		elif path[t][1] == i :
			path_two.append(path[t][0])
	path_two.sort()
	for k in path_two :
		if visit_dfs[k] == False:
			dfs(path, k, visit_dfs)

def bfs(path, i, visit_bfs) :
	queue = deque()
	queue.append(i)
	while queue :
		num = queue.popleft()
		print(num, end=' ')
		visit_bfs[num] = True
		temp = []
		for t in range(m) :
			if path[t][0] == num :
				temp.append(path[t][1])
			elif path[t][1] == num :
				temp.append(path[t][0])
		temp.sort()
		for k in temp :
			if (visit_bfs[k] == False)  :
				queue.append(k)
				visit_bfs[k] = True

dfs(path, start, visit_dfs)
print()
bfs(path, start, visit_bfs)