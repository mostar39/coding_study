import sys
n, total = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for i in range(n)]

d = [10001]*(total+1)
d[0] = 0

for i in range(n) :
	for j in range(money[i], total+1) :
		if d[j-money[i]] != 10001 :
			d[j] = min(d[j],d[j-money[i]]+1)

if d[total] == 10001 :
	print(-1)
else :
	print(d[total])