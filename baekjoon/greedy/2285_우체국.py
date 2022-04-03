import sys

n = int(sys.stdin.readline())
array = []
all_ = 0
for i in range(n) :
	temp_ = list(map(int, sys.stdin.readline().split()))
	array.append(temp_)
	all_ += temp_[1]

array.sort(key = lambda x:x[0])


temp = 0
for i in range(n) :
	temp += array[i][1]
	if temp >= all_/2 :
		print(array[i][0])
		break