import sys
n, m = map(int, sys.stdin.readline().split())
array =[list(map(int,sys.stdin.readline().split())) for i in range(n)]

for k in range(n) :
	for a in range(n) :
		for b in range(n) :
			if array[a][b]>array[a][k]+array[k][b] :
				array[a][b] = array[a][k]+array[k][b]

for _ in range(m) :
	start, end, time = list(map(int,sys.stdin.readline().split()))
	if array[start-1][end-1] <= time :
		print('Enjoy other party')
	else :
		print('Stay here')