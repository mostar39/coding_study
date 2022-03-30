import sys
sys.setrecursionlimit(10**6)
test_case = int(sys.stdin.readline())

def dfs(x,y) :
	if x<=-1 or y<=-1 or x>row or y>col :
		return False
	if [x,y] in array :
		array.remove([x,y])
		dfs(x-1,y)
		dfs(x+1,y)
		dfs(x,y+1)
		dfs(x,y-1)
		return True
	return False

for i in range(test_case) :
	row, col, k = map(int, sys.stdin.readline().split())
	array = [list(map(int,sys.stdin.readline().split())) for i in range(k)]
	jirung = 0

	for r in range(row) :
		for c in range(col) :
			if dfs(r,c) == True :
				jirung += 1

	print(jirung)
