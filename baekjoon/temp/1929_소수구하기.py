a,b = map(int,input().split())
sign = 0

for i in range(a,b+1) :
	if i == 1 :
		continue
	for j in range(2,int(i**(1/2))+1) :
		if i%j == 0 :
			sign = 1
			break
	if sign == 0 :
		print(i)
	sign = 0