n, l, w, h = map(int,input().split())

start = 0
end = max(l,w,h)

temp = 0
for _ in range(10000):

	mid = (start+end)/2
	if (l//mid) * (w//mid) * (h//mid) >= n :
		start = mid

	elif (l//mid) * (w//mid) * (h//mid)  < n :
		end = mid

print(mid)
