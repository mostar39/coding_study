n, m = map(int,input().split())

coin = []
for i in range(n) :
	coin.append(int(input()))

coin.sort(reverse=True)

count = 0
for i in range(n) :
	if m<=0 :
		break
	count = count + m//coin[i]
	m = m - coin[i]*(m//coin[i])

print(count)