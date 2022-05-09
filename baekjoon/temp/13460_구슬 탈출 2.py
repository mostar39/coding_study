import sys
n, m = map(int, sys.stdin.readline().split())
array = []
for i in range(n) :
	for j in range(m) :
	array.append(list(map(str,sys.stdin.readline().strip())))