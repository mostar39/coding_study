n = int(input())

array=[int(input()) for i in range(n)]

answer = 0

for i in range(n-2,-1,-1) :
	target = array.pop()
	if target > array[i] :
		continue
	else :
		answer += (array[i] - target) + 1
		array[i] = target - 1
print(answer)