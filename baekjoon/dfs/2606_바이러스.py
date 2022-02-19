computer_n = int(input())
edge_n = int(input())

path = []
visited = [0]*(computer_n+1)
for i in range(edge_n) :
	path.append(list(map(int,input().split())))

def dfs(path, i, visited) :

	i_list = []
	visited[i] = 1
	for k in range(len(path)) :
		if (path[k][0] == i) and  (visited[path[k][1]]==0):
			i_list.append(path[k][1])
		elif (path[k][1] == i) and  (visited[path[k][0]]==0):
			i_list.append(path[k][0])
	i_list.sort()

	for k in i_list :
		dfs(path, k, visited)

dfs(path,1,visited)
print(sum(visited)-1)

