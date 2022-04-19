import sys
n, m = map(int,sys.stdin.readline().split())
count = 0
for i in range(1,n+1) :
	if str(m) in str(i) :
		count += str(i).count(str(m))

print(count)