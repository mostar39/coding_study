import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

left = 0
right = len(array)-1
low_abs = float('inf')

real_left = 0
real_right = len(array)-1

while (left<right) :
	if low_abs == 0 :
		break
	temp = array[right] + array[left]
	if abs(temp) < abs(low_abs) :
		real_left = left
		real_right = right
		low_abs = abs(temp)
	if temp>0 :
		right = right - 1
	else :
		left = left + 1

print(array[real_left], end = ' ')
print(array[real_right])

