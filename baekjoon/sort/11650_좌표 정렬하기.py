import sys

n = int(sys.stdin.readline())
array = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
array.sort(key=lambda x:(x[0],x[1]))

for i in range(n) :
	print(array[i][0],array[i][1])