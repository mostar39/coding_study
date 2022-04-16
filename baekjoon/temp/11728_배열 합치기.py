import sys

n, m = map(int, sys.stdin.readline().split())
ar_1 = list(map(int,sys.stdin.readline().split()))
ar_2 = list(map(int,sys.stdin.readline().split()))

ar_1 = ar_1 + ar_2

ar_1.sort()

for i in range(len(ar_1)) :
	print(ar_1[i],end=' ')