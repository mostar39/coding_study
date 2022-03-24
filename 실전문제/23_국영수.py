import sys

n = int(sys.stdin.readline())
array = [sys.stdin.readline().split() for i in range(n)]

array.sort(key=lambda x:(-int(x[1]),int(x[2]), -int(x[3]), x[0]))

for i in range(len(array)) :
	print(array[i][0])