n, what = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = n-1

temp = -1

while True:
	if start > end :
		break
	mid = (start + end) // 2
	if array[mid] > what :
		end = mid-1
	elif array[mid] < what :
		start = mid + 1
	else :
		temp = mid
		end = mid-1

min_ = temp

start = min_
end = n-1

temp = -1

while True:
	if start > end :
		break
	mid = (start + end) // 2
	if array[mid] > what :
		end = mid-1
	elif array[mid] < what :
		start = mid + 1
	else :
		temp = mid
		start = mid + 1

max_ = temp

if min_ == -1 and max_ == -1 :
	print(-1)
else :
	print(max_-min_+1)


