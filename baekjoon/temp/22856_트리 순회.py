import sys
sys.setrecursionlimit(10**7)
n = int(input())
array = {}

for i in range(n) :
	num, left, right = map(int,input().split())
	array[num] = [left,right]

count = 0
visited = [False] * (n+1)
check = [False] * (n+1)

def dfs(num, what_check, baby) :
	visited[num] = True
	check[num] = what_check
	if baby[0]!= -1 :
		new_check = what_check or True
		dfs(baby[0], new_check, array[baby[0]])
	if baby[1]!= -1 :
		new_check = what_check or False
		dfs(baby[1], new_check, array[baby[1]])

for i in range(1,n+1) :
	if visited[i] == False :
		dfs(i,False, array[i])
	if i != 1 :
		if check[i] :
			count += 2
		else :
			count += 1
print(count)
