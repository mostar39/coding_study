import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(n)]

array_minus = [array[i] for i in range(len(array)) if array[i]<=0]
array_plus = [array[i] for i in range(len(array)) if array[i]>0]

array_minus.sort()

sum = 0

for i in range(0,len(array_minus),2) :
	if len(array_minus)-1 == i :
		sum += array_minus[i]
	else :
		sum= sum + array_minus[i] * array_minus[i+1]

array_plus.sort(reverse=True)

for i in range(0,len(array_plus),2) :
	if len(array_plus)-1 == i :
		sum += array_plus[i]
	elif array_plus[i+1] ==1:
		sum = sum + array_plus[i] + array_plus[i+1]
	else :
		sum= sum + array_plus[i] * array_plus[i+1]

print(sum)

