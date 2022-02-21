n = int(input())
edge = list(map(int,input().split()))
price = list(map(int, input().split()))


min_price = min(price[:len(price)-1])
min_price_index = price.index(min_price)


price_count = 0

for i in range(n-1) :
	if (min_price_index == i) :
		distance = edge[i:]
		price_count += min_price*sum(distance)
		break
	else :
		price_count += edge[i] * price[i]


print(price_count)