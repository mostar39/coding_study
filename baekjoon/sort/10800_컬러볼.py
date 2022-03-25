import sys


n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i in range(len(array)) :
	sum = 0
	temp_array = sorted(array, key=lambda x:x[1])
	start = 0
	end = len(temp_array)-1
	index = -1
	while start<=end :
		mid = (start+end)//2
		if array[i][1]>temp_array[mid][1] :
			start = mid + 1
			index = mid
		elif array[i][1]<=temp_array[mid][1] :
			end = mid - 1
	if index==-1 :
		print(0)
		continue
	for j in range(index+1) :
		if (array[i][0] != temp_array[j][0]) and (array[i][1]!=temp_array[j][1]) :
			sum+=temp_array[j][1]
	print(sum)