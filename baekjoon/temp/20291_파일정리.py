n = int(input())
array = [list(input().split('.')) for _ in range(n)]

array.sort(key=lambda x:x[1])
unique = list(set(list(zip(*array))[1]))
unique.sort()

real_start = 0
start = 0
end = len(array)-1

for i in range(len(unique)) :
	target = unique[i]
	temp = -1
	while True:
		if start > end :
			break
		mid = (start+end)//2
		if array[mid][1] == target :
			temp = mid
			start = mid+1
		else :
			end = mid-1

	print(target, (temp-real_start+1))
	start = temp + 1
	end = len(array)-1
	real_start = temp + 1
