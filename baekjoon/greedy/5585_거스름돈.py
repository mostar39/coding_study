n = 1000-int(input())

coin = [500,100,50,10,5,1]

count = 0
for i in range(len(coin)) :
	if n <= 0 :
		break
	count = count + n//coin[i]
	n -= (n//coin[i])*coin[i]


print(count)