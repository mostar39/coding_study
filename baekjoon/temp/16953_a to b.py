import sys

n, m = map(int,sys.stdin.readline().split())

count = 1

while m>n :
	if str(m)[-1] == '1' :
		count += 1
		m = int(str(m)[:-1])
	elif m % 2 == 0 :
		count += 1
		m = int(m / 2)
	elif m % 2 == 1 :
		check = 1
		break
if m == n :
	print(count)
else :
	print(-1)